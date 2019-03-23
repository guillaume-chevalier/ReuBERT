import collections
import os
from pprint import pprint

import pytest

from src import DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR
from src.infrastructure.bert.run_squad import read_predict_file_json
from src.infrastructure.trained_bert_q_a_model import TrainedBERTQuestionAnsweringModel, get_reubert_flags


def prepare_test():
    flags = get_reubert_flags()
    print(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR)
    predict_file = os.path.join(
        DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR,
        "squad_dir/dev-v2.0-beautified-only-normans.json")
    print(predict_file)
    input_data = read_predict_file_json(predict_file)
    expected_predictions = collections.OrderedDict(
        [('56ddde6b9a695914005b9628', 'France'),
         ('56ddde6b9a695914005b9629', '10th and 11th centuries'),
         ('56ddde6b9a695914005b962a', ''), ('56ddde6b9a695914005b962b',
                                            'Rollo'),
         ('56ddde6b9a695914005b962c', '10th'), ('5ad39d53604f3c001a3fe8d1', ''),
         ('5ad39d53604f3c001a3fe8d2', ''),
         ('5ad39d53604f3c001a3fe8d3', 'Normans'),
         ('5ad39d53604f3c001a3fe8d4', '')])
    bert_model = TrainedBERTQuestionAnsweringModel(flags)
    return expected_predictions, bert_model, input_data


def test_squad_gives_good_results_given_some_test_data():
    # Disable test if in CI, because it needs a downloaded model:
    if os.environ.get("CI") is not None:
        return

    expected_predictions, bert_model, input_data = prepare_test()
    pprint(input_data)

    all_predictions, all_nbest_json, scores_diff_json = bert_model.transform(
        input_data)

    pprint(all_predictions)
    pprint(all_nbest_json)
    pprint(scores_diff_json)
    # Assert false to view the printed outputs:
    # assert False
    assert all_predictions == expected_predictions


if __name__ == "__main__":
    pytest.main(__file__)
