#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    X, y = load_iris(return_X_y = True)

    model = naive_bayes.GaussianNB()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,train_size=0.80)
    
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)

    return metrics.accuracy_score(y_test, y_fitted)

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
