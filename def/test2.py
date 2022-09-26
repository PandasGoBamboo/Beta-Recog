import json, csv, pandas as pd 
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, make_scorer, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression, SGDClassifier, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score, cross_val_predict
############################ Datei laden

path = '../zdf_data/cleaned/csv/03_09/'
all = pd.read_csv(path + '03_09_zdf_dokumentation__transformed_allDocs.csv', encoding='utf-8', sep=';')

lemma_file = pd.read_csv(path + 'lemmatestframe.csv', encoding='utf-8', sep=';')
lemma = lemma_file['lemma']

all['lemma'] = lemma
# Spalte, die zum Training verwendet wird



X = all['stripped']
y = all['brand']


# Cross-Validation mit Vektorisierung und Klassifikation

kf = KFold(n_splits=10, shuffle=True)
clf = Pipeline([('vect', CountVectorizer()), ('mNB', MultinomialNB())])

y_pred = cross_val_predict(clf, X, y, cv=kf)
print(classification_report(y, y_pred))

# Printed nur den Overall-Score
#scores = cross_val_score(clf, X, y, cv=kf)


