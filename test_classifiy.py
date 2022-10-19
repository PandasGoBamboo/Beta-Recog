import pandas as pd 
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_predict, GridSearchCV
import nltk
from nltk.corpus import stopwords
from datetime import datetime
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix


# Counter für Dauer von Skriptausführung
startTime = datetime.now()
print(startTime)

############################ Datei laden

file = 'C:/Users/tschu/Desktop/BETA-RECOG/more_stripped_raw_data.pkl'

nltk.download('stopwords')
german_stop_words = stopwords.words('german') 

print('Ich roedel......')

liste = ['CHR', 'ESS', 'REP', 'REZ', 'KOM', 'INT', 'GRF', 'REZ'] 
#liste = ['REP', 'ESS', 'CHR']
data = pd.read_pickle(file)

#new = data[~data['pform'].isin(liste)]
new = data[data['pform'].isin(liste)]

#new.reset_index(drop=True, inplace=True)


all = new
#all = new.sample(n=50000, random_state=1)
#all['stripped_text'] = all['stripped_text'].str.split().str[:100].str.join(' ')
#all['stripped_text'] = all['stripped_text'].apply(lambda x: ' '.join(x.split(' ')[:300]))

texts = all['stripped_text']
#texts = all['stripped_titel'] + all['stripped_sonst_titel'] + all['stripped_text']

# Trainingsklassenaus
y = all['pform']

# Trainingsspalten
X = texts

print('X und Y geladen')


############################ Cross-Validation mit Vektorisierung, Klassifikation und Parametertuning

##### Initialisierung des KFold
# n_split =   Anzahl, wie oft Daten aufgeteilt werden
# shuffle =   Randomisiert die Daten. Da sie in der Datei nach Klassen sortiert sind,
#             muss dieser Param gesetzt werden.
# rnd_state = Eine beliebige Zahl. Dadurch wird gesichert, dass immer dieselbe Aufteilung 
#             erfolgt. 

kf = KFold(n_splits=10, shuffle=True, random_state=42)

############################ Pipeline Bestandteile

#vectorizier = CountVectorizer()
#tfidf = TfidfTransformer()
vectorizier = TfidfVectorizer()

#### Klassifikator
classifier = SGDClassifier()
#classifier = LogisticRegression()
#classifier = SVC()

scaler = StandardScaler()

pipe = Pipeline([
    ('vect', vectorizier),
    ('scaler', scaler),
    ('sgd', classifier)
    ])

params = {
    "vect__lowercase": [False],
    "vect__stop_words": [german_stop_words],
    "scaler__with_mean": [False],
    'sgd__class_weight': ['balanced'],
    'sgd__loss': ['hinge'],
    'sgd__max_iter': [5000]
    }

print('Ich fitte jetzt')
clf = GridSearchCV(pipe, param_grid = params, cv = kf )
clf.fit(X, y)
print(clf.best_params_)

print('Ich predicte jetzt')
y_pred = cross_val_predict(clf, X, y)
print(' ')

############################ Output und Visualisierungen
print('Report für: ' + 'stripped')
print(' ')
print(confusion_matrix(y, y_pred))
plot_confusion_matrix(clf, X, y_pred)  
plt.show()
print(' ')
print(classification_report(y, y_pred))


# filename = 'text_allfiles_model.sav'
# pickle.dump(clf, open(filename, 'wb'))

print(startTime - datetime.now())