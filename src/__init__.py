"""Init src directory and global variables related to data loading from relative paths."""

import os


def get_project_root():
    src = os.path.realpath(__file__)
    src_list = src.split(os.sep)
    if ":" in src_list[0]:
        src_list[0] = src_list[0] + os.sep
    idx = src_list.index("src")
    assert idx != 1, "Something is wrong."
    src_list[0] = os.sep if src_list[0] == '' else src_list[0]
    project_root = os.path.join(*src_list[:idx])
    return project_root


PROJECT_ROOT = get_project_root()
os.chdir(PROJECT_ROOT)

DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR = os.path.join(PROJECT_ROOT,
                                                     "thales-bert-gcp-bucket")
if not os.path.exists(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR):
    os.mkdir(DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR)

if __name__ == "__main__":
    """Run this file to see what the variable's values are."""
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR:",
          DOWNLOADED_THALES_BERT_GCP_BUCKET_DIR)
