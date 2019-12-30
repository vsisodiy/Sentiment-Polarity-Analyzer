# Sentiment-Polarity-Analyzer (Logistic Regression from scratch)

Description:

This code implements a working Natural Language Processing (NLP) system, i.e., a sentiment polarity analyzer, using binary logistic regression. It uses the algorithm for binary classification.

This first program is feature.py, that converts raw data (e.g., train_data.tsv, valid_data.tsv, and test_data.tsv) into formatted training, validation and test data based on the vocabulary information in the dictionary file dict.txt.

The second program is lr.fpy|java|cpp|mg, that implements a sentiment polarity analyzer using binary logistic regression. The file should learn the parameters of a binary logistic regression model that predicts a sentiment polarity (i.e. label) for the corresponding feature vector of each example. The program should output the labels of the training and test examples and calculate training and test error (percentage of incorrectly labeled examples).

How to Run:

Code1 command - python feature.py [args1...]

Where above [args1...] is a placeholder for eight command-line arguments:<train input> <validation input> <test input> <dict input> <formatted train out> <formatted validation out> <formatted test out> <feature flag>. These arguments are described in detail below:
1. <train input>: path to the training input .tsv file
2. <validation input>: path to the validation input .tsv file
3. <test input>: path to the test input .tsv file
4. <dict input>: path to the dictionary input .txt file (explained below)
5. <formatted train out>: path to output .tsv file to which the feature extractions on the training
data should be written
6. <formatted validation out>: path to output .tsv file to which the feature extractions on
the validation data should be written
7. <formatted test out>: path to output .tsv file to which the feature extractions on the test
data should be written
8. <feature flag>: integer taking value 1 or 2 that specifies whether to construct the Model 1
feature set or the Model 2 feature set (Explained below)
  
Code2 command - python lr.py [args2...]

[args2...] is a placeholder for eight command-line arguments:<formatted train input> <formatted validation input> <formatted test input> <dict input> <train out> <test out> <metrics out> <num epoch>. These arguments are described in detail below:
1. <formatted train input>: path to the formatted training input .tsv file
2. <formatted validation input>: path to the formatted validation input .tsv file
3. <formatted test input>: path to the formatted test input .tsv file
4. <dict input>: path to the dictionary input .txt file
5. <train out>: path to output .labels file to which the prediction on the training data should be written
6. <test out>: path to output .labels file to which the prediction on the test data should be written
7. <metrics out>: path of the output .txt file to which metrics such as train and test error should be written
8. <num epoch>: integer specifying the number of times SGD loops through all of the training data (e.g., if <num epoch> equals 5, then each training example will be used in SGD 5 times).
  
Dictionary/Vocablary: It is simply a .txt file with all the words from your training file
  
Model 1: This model defines a probability distribution over the current label y(i) using the parameters and a bag-of-word feature vector indicating which word in vocabulary of the dictionary occurs at least once in the example. The entry in the indicator vector associated to the occurring word will set to one (otherwise, it is zero). This bag-of-word model should be used when <feature flag> is set to 1.
  
Model 2: This model defines a probability distribution over the current label y(i) using the parameters and a trimmed bag-of-word feature vector indicating (1) which word in vocabulary Vocab of the dictionary occurs in the example x(i), AND (2) the count of the word is LESS THAN (<) threshold t. The entry in the indicator vector associated to the word that satisfies both conditions will set to one (otherwise, it is zero, including no shown and high-frequent words). This trimmed bag-of-word model should be used when <feature flag> is set to 2. In this code, I have used the constant trimming threshold t = 4.
  
