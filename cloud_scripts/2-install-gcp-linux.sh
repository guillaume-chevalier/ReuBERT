#!/usr/bin/env bash

# Instructions here: 
# https://cloud.google.com/storage/docs/gsutil_install#linux

curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init

