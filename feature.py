import sys
from collections import OrderedDict

vocab = open(sys.argv[4], "r+")

vocab1 = vocab.readlines()

vocab_words = []
vocab_index = []
for line in vocab1:
    vocab_words.append(line.split()[0])
    vocab_index.append(line.split()[1])

vocab_dict = dict(zip(vocab_words, vocab_index))

def feature(input, output, flag):
    file = open(input, "r+")
    file1 = file.readlines()
    
    data = []
    for line in file1:
        data.append(line.split("\t"))
        
    
    file2 = open(output, "w")
    
    if flag == '1':
        for line in data:
            review = list(OrderedDict.fromkeys(line[1].split()))
            file2.writelines(line[0]+ "\t")
            for i in range(len(review)):
                if review[i].strip() in vocab_dict:
                    file2.writelines(vocab_dict[review[i].strip()]+ ":1"+ "\t")
            file2.writelines("\n")
            
        file2.close()
        
    if flag == '2':
        for line in data:
            review = line[1].split()
            review1 = list(OrderedDict.fromkeys([v for v in review if review.count(v) < 4]))
            file2.writelines(line[0]+ "\t")
            for i in range(len(review1)):
                if review1[i].strip() in vocab_dict:
                    file2.writelines(vocab_dict[review1[i].strip()]+ ":1"+ "\t")
            file2.writelines("\n")
            
        file2.close()
            
feature(sys.argv[1], sys.argv[5], sys.argv[8])
feature(sys.argv[2], sys.argv[6], sys.argv[8])
feature(sys.argv[3], sys.argv[7], sys.argv[8])






