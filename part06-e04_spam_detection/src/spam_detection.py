#!/usr/bin/env python3

from gzip import open
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def extract_array(fname, fraction):
    if fraction > 1 or fraction < 0:
        return None

    with open(fname) as f:
        fopen = f.readlines()
        num_array = int(fraction * len(fopen))
        fname_list = fopen[:num_array]
        return_list = [i.decode(encoding='UTF-8') for i in fname_list]
        return return_list

def spam_detection(random_state=0, fraction=0.1):
    ham = extract_array('src/ham.txt.gz', fraction)
    spam = extract_array('src/spam.txt.gz', fraction)
    concat_list = np.concatenate((ham, spam))

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(concat_list).toarray()
    y = np.zeros(len(X))
    y[len(ham):] = 1

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)
    result = accuracy_score(y_test, y_fitted)
    misclassified = np.sum(y_test != y_fitted)
    return (result, len(X_test), misclassified)

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
