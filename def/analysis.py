import json, csv, pandas as pd 
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.preprocessing import StandardScaler
############################ Datei laden
all = pickle.load(open("allDocs.p", "rb"))

# Spalte, die zum Training verwendet wird
X = all['text']

# Liste der Labels
y = all['brand']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)


############################ Vektorisierung
cv = CountVectorizer()

cv.fit(X_train)

X_train = cv.transform(X_train)
X_test = cv.transform(X_test)


############################ Klassifikation
"""
# Naiver Bayes

mNB = MultinomialNB()
mNB.fit(X_train, y_train)
y_pred = mNB.predict(X_test)


# Logistische Regression

logReg = LogisticRegression()
logReg.fit(X_train, y_train)
y_pred = logReg.predict(X_test)


# Support Vektor Maschine

svm = SGDClassifier()
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

############################ Output der Confusionsmatrix
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred))
"""
classifier = [
    MultinomialNB(),
    LogisticRegression(max_iter=200),
    SGDClassifier()
]

for clf in classifier:
    if clf != LogisticRegression():
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print('accuracy %s' % accuracy_score(y_pred, y_test))
        print(classification_report(y_test, y_pred))
        print('--------------------------------------------------------------------------')
    else:
        scaler = StandardScaler()
        X_train = scaler.fit(X_train)
        X_test = scaler.fit(X_test)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print('accuracy %s' % accuracy_score(y_pred, y_test))
        print(classification_report(y_test, y_pred))
        print('--------------------------------------------------------------------------')