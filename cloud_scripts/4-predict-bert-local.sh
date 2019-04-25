#!/usr/bin/env bash

# Start by downloading cd-ing into BERT: 
# git clone https://github.com/google-research/bert.git
cd bert

# Variables
export BERT_BASE_DIR="../thales-bert/bert_base_dir"
export BERT_LARGE_DIR="../thales-bert/bert_base_dir"
export BUCKET_NAME="../thales-bert/squad_large/"
export SQUAD_DIR="../thales-bert/squad_dir"
export OUTPUT_DIR="../thales-bert/output_dir/"

export THRESH=-3

# Generate predictions.
python3 run_squad.py \
  --vocab_file=../thales-bert/bert_base_dir/vocab.txt \
  --bert_config_file=../thales-bert/bert_base_dir/bert_config.json \
  --init_checkpoint=../thales-bert/squad_large/model.ckpt-10859 \
  --do_train=False \
  --do_predict=True \
  --predict_file=../thales-bert/squad_dir/dev-v2.0-beautified-only-normans.json \
  --train_batch_size=1 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=../thales-bert/output_dir/ \
  --use_tpu=False \
  --version_2_with_negative=True \
  --null_score_diff_threshold=-3


# Same command as above, with variables (less verbose for debugging): 
# python3 run_squad.py \
#   --vocab_file=$BERT_LARGE_DIR/vocab.txt \
#   --bert_config_file=$BERT_LARGE_DIR/bert_config.json \
#   --init_checkpoint=$BUCKET_NAME/model.ckpt-10859 \
#   --do_train=False \
#   --do_predict=True \
#   --predict_file=../thales-bert/squad_dir/dev-v2.0-beautified-only-normans.json \
#   --train_batch_size=1 \
#   --learning_rate=3e-5 \
#   --num_train_epochs=2.0 \
#   --max_seq_length=384 \
#   --doc_stride=128 \
#   --output_dir=$OUTPUT_DIR \
#   --use_tpu=False \
#   --version_2_with_negative=True \
#   --null_score_diff_threshold=$THRESH


# Evaluate prediction's performances :

curl https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/ > evaluate-v2.0.py

python3 evaluate-v2.0.py ../dev-v2.0-beautified-only-normans.json $OUTPUT_DIR/predictions.json --na-prob-file $OUTPUT_DIR/null_odds.json

