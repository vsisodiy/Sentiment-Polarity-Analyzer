
import sys
import math

vocab = open(sys.argv[4], "r+")

vocab1 = vocab.readlines()

vocab_words = []
vocab_index = []
for line in vocab1:
    vocab_words.append(line.split()[0])
    vocab_index.append(line.split()[1])
    
vocab_dict = dict(zip(vocab_words, vocab_index))

def sgm(x):
    return 1/(1 + math.exp(-x))

def data_prep(file):
    label = []
    dict_list = []
    for line in file:
        z = line.split('\t').strip()
        label.append(z[0])
        dict_itr = {"-1":"1"}
        for i in range(1, len(z)):
            h = z[i].split(":")
            dict_itr[h[0]] = h[1]
        dict_list.append(dict_itr)
    return label, dict_list

def sparse_dot(X, theta):
    prod = 0.0
    for p in X:
        prod += theta[int(p)]
    return prod

def sgd(label, dict_list, theta):
    for rnd in range(len(dict_list)):
        y = label[rnd]
        X = dict_list[rnd]
        dot_prod = sparse_dot(X, theta)
        z = y - sgm(dot_prod)
        list_temp = [z for i in range(len(X.keys()))]
        grad_theta = dict(zip(X.keys(), list_temp))
    for p,q in grad_theta.items():
        theta[int(p)] += 0.1*q
            
    
#i need the actual labels and the predicted labels
#actual labels I can get from the data_prep function for each file - it will also give me the dict_list
#predicted labels - round(sgm(sparse_dot(theta, x)))

def predict(theta, label, input_dict):
    pred_label = [int(round(sgm(sparse_dot(theta, x)))) for x in input_dict]
    count = 0
    for i in range(len(label)):
        if (pred_label[i] != int(label[i])):
            count+=1
    error = count/len(label)
    return error, pred_label




trainlabels, train_dict = data_prep(sys.argv[1])

k = 0
theta = [0 for i in range((len(vocab_dict)+1))]

while(k < sys.argv[8]):
    sgd(trainlabels, train_dict, theta)
    k +=1
    
testlabels, test_dict = data_prep(sys.argv[3])

train_error, train_label = predict(theta, trainlabels, train_dict)
test_error, test_label = predict(theta, trainlabels, train_dict)

file4 = open(sys.argv[7], "w")
file4.writelines("error(train): " + str(train_error) + "\n")
file4.writelines("error(test): " + str(test_error))
file4.close()

file5 = open(sys.argv[5], "w")
for i in range(train_label):
    file5.writelines(str(train_label[i]) + "\n")
file5.close()

file6 = open(sys.argv[6], "w")
for i in range(test_label):
    file6.writelines(str(test_label[i]) + "\n")
file6.close()




