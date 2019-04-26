# ReuBERT

ReuBERT is a chatbot based on BERT and the SQuAD dataset, built for Thales in the context of a coursework. The interactions happen in two phases:
- Phase 1: the chatbot acquires information from the user (states 1 and 2)
- Phase 2: the user asks questions and the chatbot answers according to the information it has been given in the first Phase (states 3 and 4)

![](states.png)

## Example usage in the command line:

Running `python main.py`:

```
ReuBERT[greeting]:~$ Welcome! What would you like to talk about? Note: when you are ready to ask questions, just say 'I am ready to ask questions.'
You[enter information]:~$

William Shakespeare was an English poet, playwright and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist. He is often called England's national poet and the "Bard of Avon". His extant works, including collaborations, consist of approximately 39 plays, 154 sonnets, two long narrative poems, and a few other verses, some of uncertain authorship. His plays have been translated into every major living language and are performed more often than those of any other playwright.

ReuBERT[gather information]:~$ Can you give me more information please?
You[enter information]:~$

Shakespeare was born and raised in Stratford-upon-Avon, Warwickshire.At the age of 18, he married Anne Hathaway, with whom he had three children : Susanna and twins Hamnet and Judith. Sometime between 1585 and 1592, he began a successful career in London as an actor, writer, and part-owner of a playing company called the Lord Chamberlain's Men, later known as the King's Men. At age 49 (around 1613), he appears to have retired to Stratford, where he died three years later.

ReuBERT[gather information]:~$ Can you give me more information please?
You[enter information]:~$

Few records of Shakespeare's private life survive; this has stimulated considerable speculation about such matters as his physical appearance, his sexuality, his religious beliefs, and whether the works attributed to him were written by others. Such theories are often criticised for failing to adequately note that few records survive of most commoners of the period.

ReuBERT[gather information]:~$ Can you give me more information please?
You[enter information]:~$

I am ready to ask questions.

ReuBERT[gather information]:~$ Ok. Ask me your questions. Note: you can quit the application at anytime by saying 'I have no more questions to ask.'
You[enter question]:~$

Where was William Shakespeare born ?

ReuBERT[answer question]:~$ stratford
You[enter question]:~$

When did William Shakespeare retire ?

ReuBERT[answer question]:~$ 1613
You[enter question]:~$

What is the name of Shakespeare's playing company ?

ReuBERT[answer question]:~$ the Lord Chamberlain's Men
You[enter question]:~$

Who is Shakespeare's wife

ReuBERT[answer question]:~$ anne hathaway
You[enter question]:~$

How Shakespeare was called ?

ReuBERT[answer question]:~$ England's national poet
You[enter question]:~$

How many plays did Shakespeare write ?

ReuBERT[answer question]:~$ approximately 39
You[enter question]:~$

Who were Shakespeare childrens ?

ReuBERT[answer question]:~$ judith
You[enter question]:~$

When did Shakespeare had  childrens ?

ReuBERT[answer question]:~$ between 1585 and 1592
You[enter question]:~$

I have no more questions to ask.

ReuBERT[goodbye]:~$ See you later!
```

## Setup

### Virtual Environment

You must first setup a **Python 3.6** virtualenv.
1. Install virtual environments: `pip install virtualenv`.
2. Create the "env" virtual environment in the root of the project: `virtualenv env -p python3`.
3. You may now activate it as needed, and configure the new virtualenv in your IDE: `source env/bin/activate`.
4. Install requirements: `pip install -r requirements.txt.`

### Set up pre-commit hooks (only if you intend to develop and push new commits)

1. Ensure that the virtual environment's name is "env".
2. Modify your local git configuration to point the correct emplacement of the project hooks
    > Run the following command in the terminal at the project root:

    `git config core.hookspath .githooks`
3. Everytime you create a new commit, you should see the output of yapf execution which reformats all source files properly.

### Fine-tuning BERT on the SQuAD dataset in the cloud on a TPU

See the steps 1 and 2 in the cloud directory's [README.md](cloud_scripts/README.md).

You may skip this step if a member of your team already did this step, as it is compute-intensive and costly.

\# TODO: Google Drive link or other link for the data folder.

### Download the fine-tuned BERT's weights for local CPU usage of the model

See the steps 3, 4 and 5 in the cloud directory's [README.md](cloud_scripts/README.md). Basically, you need to download the trained BERT model and place it at some place under the `./thales-bert-gcp-bucket` directory here.

### Download Spacy NLP model

Run `python -m spacy download en_core_web_sm` in the virtual environment to setup the spacy dependency.

### Run tests

Once install, verify your installation by running tests within the virtualenv using the command `./run_tests.sh` when placed in the root of the project. Note: you might need to run this command before running tests: if you run them in an IDE or without the script: `export PYTHONPATH=$PYTHONPATH:$(pwd)`.

### Enjoy!

You can now run the main, such as by doing `python main.py`, to use the Question-Answering chatbot.

## Licenses

### Libs

- [BERT](https://github.com/google-research/bert): Apache 2.0
- [TensorFlow](https://www.tensorflow.org/): Apache 2.0
- [scikit-learn](https://scikit-learn.org/stable/): BSD-3-Clause
- [spaCy](https://spacy.io/): MIT
- [en_core_web_sm](https://spacy.io/models/en#en_core_web_sm): MIT

### Data :

- [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/): CC-BY-SA 4.0
- [CoQA](https://stanfordnlp.github.io/coqa/): CC-BY-SA 4.0

### Other data :

- [William_Shakespeare](https://en.wikipedia.org/wiki/William_Shakespeare): CC BY-SA 3.0 Unported License
- [Abraham Lincoln](https://en.wikipedia.org/wiki/Abraham_Lincoln): CC BY-SA 3.0 Unported License
- [Barack Obama](https://en.wikipedia.org/wiki/Barack_Obama): CC BY-SA 3.0 Unported License

## Authors

- Guillaume Chevalier
- Taha Racicot
- Julie Tétrault
