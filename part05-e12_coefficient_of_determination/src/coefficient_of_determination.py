#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model

def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    X = df.loc[:, "X1":"X5"]
    y = df.Y

    reg = linear_model.LinearRegression(fit_intercept=True).fit(X, y)
    score = reg.score(X, y)

    scores = [score]

    for i in range(len(X.columns)):
        a = X.iloc[:, i].values.reshape(-1, 1)
        reg.fit(a, y)
        scores.append(reg.score(a, y))

    return scores
    
def main():
    x = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {x[0]}")
    for i in range(1, len(x)):
        print(f"R2-score with feature(s) X{i}: {x[i]: .4f}")

if __name__ == "__main__":
    main()
