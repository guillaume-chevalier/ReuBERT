# Cloud code

## Instructions

How to run: execute those files in order.
- 1-download_and_train_bert.sh
- 2-install-gcp-linux.sh
- 3-download-bert-bucket-to-local-folder.sh
- 4-predict-bert-local.sh
- 5-mv-gcp-dir.sh

You may want to copy and try to run each command manually instead of executing those files in batch like this. This is to ensure each step is successful.

Especially for the 5th .sh file, you'll need to merge the downloaded code to the good local folder in `../thales-bert-gcp-bucket` from the downloaded `./thales-bert` GCP bucket.

## Hardware

Running this code requires renting a TPUv2 on Google Cloud Platform (GCP). The current folder is left as historic code if someone ever needs to re-train BERT on the SQuAD as we did. For what remains, the team will (or has already) refactor BERT's open-source code into the `../src` repository of the present project. Follow the instructions on [this page](https://github.com/google-research/bert) under the SQuAD 2 section.

## Licenses

- [BERT](https://github.com/google-research/bert): Apache 2.0
- [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/): CC-BY-SA 4.0
