import os

import tensorflow as tf

from src.domain.pipeline_steps.question_answering_model import QuestionAnsweringModelInterface
from src.infrastructure.bert import modeling, tokenization
from src.infrastructure.bert.run_squad import validate_flags_or_throw, model_fn_builder, do_predict, \
    write_predictions, Flags
from src import DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR


def get_reubert_flags():
    # Our settings on top of the default ones.
    flags = Flags()
    flags.vocab_file = os.path.join(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR, "bert_base_dir/vocab.txt")
    flags.bert_config_file = os.path.join(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR, "bert_base_dir/bert_config.json")
    flags.init_checkpoint = os.path.join(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR, "squad_large/model.ckpt-10859")
    flags.predict_batch_size = 1
    flags.output_dir = os.path.join(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR, "output_dir/")
    flags.version_2_with_negative = True
    flags.null_score_diff_threshold = -3  # TODO: adjust this to try to get a better score. Must be between -1 and -5.
    return flags


class TrainedBERTQuestionAnsweringModel(QuestionAnsweringModelInterface):

    def __init__(self, flags):
        self.flags = flags
        tf.logging.set_verbosity(tf.logging.INFO)

        bert_config = modeling.BertConfig.from_json_file(flags.bert_config_file)

        validate_flags_or_throw(flags, bert_config)

        tf.gfile.MakeDirs(flags.output_dir)

        self.tokenizer = tokenization.FullTokenizer(
            vocab_file=flags.vocab_file, do_lower_case=flags.do_lower_case)

        is_per_host = tf.contrib.tpu.InputPipelineConfig.PER_HOST_V2
        run_config = tf.contrib.tpu.RunConfig(
            cluster=None,
            master=flags.master,
            model_dir=flags.output_dir,
            save_checkpoints_steps=flags.save_checkpoints_steps,
            tpu_config=tf.contrib.tpu.TPUConfig(
                iterations_per_loop=flags.iterations_per_loop,
                num_shards=flags.num_tpu_cores,
                per_host_input_for_training=is_per_host))

        model_fn = model_fn_builder(
            bert_config=bert_config,
            init_checkpoint=flags.init_checkpoint,
            use_one_hot_embeddings=False)

        # If TPU is not available, this will fall back to normal Estimator on CPU
        # or GPU.
        self.estimator = tf.contrib.tpu.TPUEstimator(
            use_tpu=False,
            model_fn=model_fn,
            config=run_config,
            train_batch_size=flags.train_batch_size,
            predict_batch_size=flags.predict_batch_size)

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        all_results, eval_examples, eval_features = do_predict(self.flags, self.estimator, self.tokenizer, X)

        all_predictions, all_nbest_json, scores_diff_json = write_predictions(
            self.flags, eval_examples, eval_features, all_results,
            self.flags.n_best_size, self.flags.max_answer_length,
            self.flags.do_lower_case
        )

        return all_predictions, all_nbest_json, scores_diff_json

    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X, y)
