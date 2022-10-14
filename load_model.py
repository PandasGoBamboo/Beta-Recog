import pandas as pd 
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, make_scorer, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression, SGDClassifier, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler, Binarizer
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV
from datetime import datetime
import pickle

filename = 'C:/Users/tschu/Desktop/BETA-RECOG/Modelle/model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
test = ['Interview mit Hans Gerd Stoiber und der Mariachi Band']
result = loaded_model.score(test.values)
print(result)