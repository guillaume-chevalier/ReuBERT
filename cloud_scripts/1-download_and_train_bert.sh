#!/usr/bin/env bash

# TRAIN BERT
# Note: you must download BERT and SQuAD in the appropriate folders in GCP bucket. 

# Here is a command to create a vm instance with tpu:
# ctpu up --name=bert --project=bert --zone=us-central1-b #todo : set memmory to 100GB

git clone https://github.com/google-research/bert.git
cd bert
rm -rf .git  # not to mess with nested respos if commiting things.

# Variables
export BERT_BASE_DIR="gs://thales-bert/bert_base_dir"
export BERT_LARGE_DIR="gs://thales-bert/bert_base_dir"
export TPU_NAME="bert"
export BUCKET_NAME="gs://thales-bert/squad_large/"
export SQUAD_DIR="gs://thales-bert/squad_dir"
export TPU_NAME="grpc://10.240.1.2:8470"


# Fine-tune BERT

python run_squad.py \
  --vocab_file=$BERT_LARGE_DIR/vocab.txt \
  --bert_config_file=$BERT_LARGE_DIR/bert_config.json \
  --init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
  --do_train=True \
  --train_file=$SQUAD_DIR/train-v2.0.json \
  --do_predict=True \
  --predict_file=$SQUAD_DIR/dev-v2.0.json \
  --train_batch_size=24 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=$BUCKET_NAME \
  --use_tpu=True \
  --tpu_name=$TPU_NAME \
  --version_2_with_negative=True


export THRESH=-3  # TODO: adjust this maybe. Typical values are between -1.0 and -5.0.

python run_squad.py \
  --vocab_file=$BERT_LARGE_DIR/vocab.txt \
  --bert_config_file=$BERT_LARGE_DIR/bert_config.json \
  --init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
  --do_train=False \
  --train_file=$SQUAD_DIR/train-v2.0.json \
  --do_predict=True \
  --predict_file=$SQUAD_DIR/dev-v2.0.json \
  --train_batch_size=24 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=$BUCKET_NAME \
  --use_tpu=True \
  --tpu_name=$TPU_NAME \
  --version_2_with_negative=True \
  --null_score_diff_threshold=$THRESH



# The code below after the exit is dead code. 
# TODO: cleanup this shell script...
exit



export SQUAD_DIR="./squad_data"

# Download dataset
mkdir $SQUAD_DIR
cd $SQUAD_DIR
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
wget https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json
curl https://worksheets.codalab.org/rest/bundles/0x6b567e1cf2e041ec80d7098f031c5c9e/contents/blob/ > evaluate-v2.0.py
cd ..


# Download pretrained BERT
# mkdir $BERT_BASE_DIR
# cd $BERT_BASE_DIR
# wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-24_H-1024_A-16.zip
# unzip uncased_L-24_H-1024_A-16.zip
# mv uncased_L-24_H-1024_A-16/* .
# cd ..

python $SQUAD_DIR/evaluate-v2.0.py $SQUAD_DIR/dev-v2.0.json $SQUAD_DIR/predictions.json --na-prob-file $SQUAD_DIR/null_odds.json


# TODO: serve predictions after training: 
# python run_squad.py \
#   --vocab_file=$BERT_LARGE_DIR/vocab.txt \
#   --bert_config_file=$BERT_LARGE_DIR/bert_config.json \
#   --init_checkpoint=$BERT_LARGE_DIR/bert_model.ckpt \
#   --do_train=False \
#   --train_file=$SQUAD_DIR/train-v2.0.json \
#   --do_predict=True \
#   --predict_file=$SQUAD_DIR/dev-v2.0.json \
#   --train_batch_size=24 \
#   --learning_rate=3e-5 \
#   --num_train_epochs=2.0 \
#   --max_seq_length=384 \
#   --doc_stride=128 \
#   --output_dir=$BUCKET_NAME \
#   --use_tpu=True \
#   --tpu_name=$TPU_NAME \
#   --version_2_with_negative=True \
#   --null_score_diff_threshold=$THRESH

