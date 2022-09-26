import json, csv, pandas as pd 
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
from nltk.corpus import stopwords

german_stop_words = frozenset([
        "aber",
        "alle",
        "allem",
        "allen",
        "aller",
        "alles",
        "als",
        "also",
        "am",
        "an",
        "ander",
        "andere",
        "anderem",
        "anderen",
        "anderer",
        "anderes",
        "anderm",
        "andern",
        "anderr",
        "anders",
        "auch",
        "auf",
        "aus",
        "bei",
        "bin",
        "bis",
        "bist",
        "da",
        "damit",
        "dann",
        "der",
        "den",
        "des",
        "dem",
        "die",
        "das",
        "daß",
        "derselbe",
        "derselben",
        "denselben",
        "desselben",
        "demselben",
        "dieselbe",
        "dieselben",
        "dasselbe",
        "dazu",
        "dein",
        "deine",
        "deinem",
        "deinen",
        "deiner",
        "deines",
        "denn",
        "derer",
        "dessen",
        "dich",
        "dir",
        "du",
        "dies",
        "diese",
        "diesem",
        "diesen",
        "dieser",
        "dieses",
        "doch",
        "dort",
        "durch",
        "ein",
        "eine",
        "einem",
        "einen",
        "einer",
        "eines",
        "einig",
        "einige",
        "einigem",
        "einigen",
        "einiger",
        "einiges",
        "einmal",
        "er",
        "ihn",
        "ihm",
        "es",
        "etwas",
        "euer",
        "eure",
        "eurem",
        "euren",
        "eurer",
        "eures",
        "für",
        "gegen",
        "gewesen",
        "hab",
        "habe",
        "haben",
        "hat",
        "hatte",
        "hatten",
        "hier",
        "hin",
        "hinter",
        "ich",
        "mich",
        "mir",
        "ihr",
        "ihre",
        "ihrem",
        "ihren",
        "ihrer",
        "ihres",
        "euch",
        "im",
        "in",
        "indem",
        "ins",
        "ist",
        "jede",
        "jedem",
        "jeden",
        "jeder",
        "jedes",
        "jene",
        "jenem",
        "jenen",
        "jener",
        "jenes",
        "jetzt",
        "kann",
        "kein",
        "keine",
        "keinem",
        "keinen",
        "keiner",
        "keines",
        "können",
        "könnte",
        "machen",
        "man",
        "manche",
        "manchem",
        "manchen",
        "mancher",
        "manches",
        "mein",
        "meine",
        "meinem",
        "meinen",
        "meiner",
        "meines",
        "mit",
        "muss",
        "musste",
        "nach",
        "nicht",
        "nichts",
        "noch",
        "nun",
        "nur",
        "ob",
        "oder",
        "ohne",
        "sehr",
        "sein",
        "seine",
        "seinem",
        "seinen",
        "seiner",
        "seines",
        "selbst",
        "sich",
        "sie",
        "ihnen",
        "sind",
        "so",
        "solche",
        "solchem",
        "solchen",
        "solcher",
        "solches",
        "soll",
        "sollte",
        "sondern",
        "sonst",
        "über",
        "um",
        "und",
        "uns",
        "unse",
        "unsem",
        "unsen",
        "unser",
        "unses",
        "unter",
        "viel",
        "vom",
        "von",
        "vor",
        "während",
        "war",
        "waren",
        "warst",
        "was",
        "weg",
        "weil",
        "weiter",
        "welche",
        "welchem",
        "welchen",
        "welcher",
        "welches",
        "wenn",
        "werde",
        "werden",
        "wie",
        "wieder",
        "will",
        "wir",
        "wird",
        "wirst",
        "wo",
        "wollen",
        "wollte",
        "würde",
        "würden",
        "zu",
        "zum",
        "zur",
        "zwar",
        "zwischen"
      ])

############################ Datei laden

path = '../zdf_data/cleaned/csv/03_09/'
all = pd.read_csv(path + '03_09_zdf_dokumentation__transformed_allDocs.csv', encoding='utf-8', sep=';')

# Datei mit Lemma laden
lemma_file = pd.read_csv(path + 'lemmatestframe.csv', encoding='utf-8', sep=';')
lemma = lemma_file['lemma']
all['lemma'] = lemma

# Spalte mit Text, die zum Training verwendet wird
all_prePro = [
    'stripped',
    'stemmed',
    'lemma'
    ]

# Trainingsklassen
y = all['brand']

############################ Cross-Validation mit Vektorisierung, Klassifikation und Parametertuning

##### Initialisierung des KFold
# n_split =   Anzahl, wie oft Daten aufgeteilt werden
# shuffle =   Randomisiert die Daten. Da sie in der Datei nach Klassen sortiert sind,
#             muss dieser Param gesetzt werden.
# rnd_state = Eine beliebige Zahl. Dadurch wird gesichert, dass immer dieselbe Aufteilung 
#             erfolgt. 

kf = KFold(n_splits=10, shuffle=True, random_state=42)

##### GridSearchCV biete Möglichkeit verschiedene Parameter zu testen

# Vektorisierungsmethode 
vectorizier = CountVectorizer()
onehot = Binarizer()
# Klassifikator
classifier = MultinomialNB()

pipe = Pipeline([
    ('vect', vectorizier),
    #('tfidf', TfidfTransformer()),
    ('mNB', classifier)
    ])

params = {
    "vect__lowercase": [False],
    "vect__stop_words": [german_stop_words],
    "mNB__alpha": [1.0]
    }

clf = GridSearchCV(pipe, param_grid = params, cv = kf )

# Trainingsspalten
X = all['stripped']
# Pipeline für den Klassifikator
y_pred = cross_val_predict(clf, X, y)

clf.fit(X, y)


print('Report für: ' + 'stripped')

print(' ')

print(classification_report(y, y_pred))

#print(clf.best_params_)

"""
for text in all_prePro:


    # Printed nur den Overall-Score
    #scores = cross_val_score(clf, X, y, cv=kf)
"""