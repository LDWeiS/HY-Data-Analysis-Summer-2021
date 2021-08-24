#!/usr/bin/env python3

from collections import Counter
import urllib.request
from numpy.core.defchararray import istitle

from numpy.lib.npyio import load
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = sorted(set(alphabet))

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    columns=len(alphabet)
    n=a.shape[0]
    f=np.zeros((n, columns))
    for i, s in enumerate(a):
        counts=Counter(s)
        for j, c in enumerate(alphabet):
            f[i, j] = counts[c]
    return f

    # vectorizer = CountVectorizer(token_pattern=r"(?u)\w|-", analyzer='char', vocabulary=alphabet_set)
    # temp = vectorizer.transform(a).toarray()
    # final_array = np.hstack((temp[:, 1:], temp[:, 0].reshape(-1, 1)))
    # return final_array

def contains_valid_chars(s):
    return alphabet_set.issuperset(s)

def get_features_and_labels():
    # Finnish words
    fin_set = load_finnish()
    fin_lower = [word.lower() for word in fin_set]
    fin_final = [word for word in fin_lower if contains_valid_chars(word)]
    finnish_feat = get_features(fin_final)
    finnish_targ = np.zeros((len(fin_final), 1))   

    #English words
    eng_set = list(load_english())
    eng_lower = [word.lower() for word in eng_set if word[0].islower()]
    eng_final = [word for word in eng_lower if contains_valid_chars(word)]
    english_feat = get_features(eng_final)
    english_targ = np.ones((len(eng_final), 1))
  
    # Features and target
    targ = np.concatenate((finnish_targ, english_targ))
    feat = np.concatenate((finnish_feat, english_feat))

    return feat, targ

def word_classification():
    feature_matrix, labels = get_features_and_labels()
    model = MultinomialNB()
    selector = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    score = cross_val_score(model, feature_matrix, np.ravel(labels), cv=selector)
    return score


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
