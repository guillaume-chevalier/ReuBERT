# Thales-Bert

## Setup

### 1. Virtual Environment

You must first setup a **Python 3.6** virtualenv.
1. Install virtual environments: `pip install virtualenv`.
2. Create the "env" virtual environment in the root of the project: `virtualenv env -p python3`.
3. You may now activate it as needed, and configure the new virtualenv in your IDE: `source env/bin/activate`.
4. Install requirements: `pip install -r requirements.txt.`

### 2. Fine-tuning BERT on the SQuAD dataset in the cloud on a TPU

See the steps 1 and 2 in the cloud directory's [README.md](cloud_scripts/README.md).

You may skip this step if a member of your team already did this step, as it is compute-intensive and costly.

### 3. Download the fine-tuned BERT's weights for local CPU usage of the model

See the steps 3, 4 and 5 in the cloud directory's [README.md](cloud_scripts/README.md). Basically, you need to download the trained BERT model and place it at some place under the `./thales-bert-gcp-bucket` directory here.

### 4. Run tests

Once install, verify your installation by running tests within the virtualenv using the command `./run_tests.sh` when placed in the root of the project.

### 5. Enjoy

You can now run the main, such as by doing `python main.py`, to use the Question-Answering chatbot.
