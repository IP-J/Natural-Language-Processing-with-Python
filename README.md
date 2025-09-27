# Natural-Language-Processing-with-Python

## Problem 1: TF-IDF
Implement TF-IDF using Python, Numpy, Pandas or whatever text cleaning library is required.
The TF-IDF is the product of two statistics: term frequency and inverse document frequency. There are various ways of determining the exact values of both statistics.

## Problem 2: Task
Implement legal case–type classification on a legal case corpus. The corpus contains 39 155 legal cases including 22 776 taken from the United States supreme court.
You can find more details about the dataset at the following link:
• OSFHOME. (2022). SigmaLaw — large legal text corpus and word embeddings: https://osf.io/qvg8s/
Implement classification using the necessary libraries with the features being GloVe word embeddings using Gensim as demonstrated below.
Report the accuracy and F1 score (micro- and macro-averaged).

Dataset:

The dataset can be downloaded here - https://osf.io/qvg8s/files/osfstorage. The files of interest are Map.txt, preprocessed_case[cases_29404].zip
The cases are categorised into 8 categories, but you are required to use a subset of those, i.e., only three categories and a subset of cases within those three categories.
Use the code load_unique_cases.py to load a Pandas DataFrame with two columns path and label. Use these files folders/files only. 

Document representation
Convert words after cleaning into their embeddings, then take the average of all the words in a case (document) to end up with single vector representing each case. The case vector is then used for case classification.
In the process of finding the embeddings for each word, you can ignore out-of-vocabulary words.

## Problem 3: POS for classification
Robots and chat bots receive different commands to do certain tasks.
Write a simple program that receives interactions in the form of a sentence and returns:
• a tuple of (command, object) if the sentence is a command
• none if the sentence is not a command.
To write this function, you can utilise a part-of-speech tagger or named-entity recogniser from libraries like NLTK and Spacy.
Consider the following example sentences:
• Commands:
– Grab the book.
– Fetch the ball.
– Open the jar.
– Can you hand this spoon to John?
• Not commands:
– Hey, how is it going?
– How is your day today?
– Do you like the weather?
This list is not exhaustive; your function should be able to handle more cases.
Expected outcome:
1. A function that performs the task.
2. If your function has limitations, highlight those limitations with examples.
