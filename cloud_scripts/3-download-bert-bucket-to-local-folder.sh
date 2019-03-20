#!/usr/bin/env bash

# Inspired from: https://stackoverflow.com/questions/11640637/download-files-and-folders-from-google-storage-bucket-to-a-local-folder

gsutil -m cp -R gs://thales-bert .

