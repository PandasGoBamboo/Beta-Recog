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
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV
from nltk.corpus import stopwords
from datetime import datetime


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

# Counter für Dauer von Skriptausführung
startTime = datetime.now()

############################ Datei laden

file = 'C:/Users/tschu/Desktop/BETA-RECOG/stemmed_raw_data.pkl'

print('Ich roedel......')

data = pd.read_pickle(file)
all = data.sample(n=10000, random_state=1)

# Trainingsklassen
y = all['pform']

# Trainingsspalten
X = all['stripped_text']

print('X und Y geladen')


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
#vectorizier = TfidfVectorizer()

# Scaler
scaler = StandardScaler()

tfidf = TfidfTransformer()

# Klassifikator
classifier = LogisticRegression() 

pipe = Pipeline([
    ('vect', vectorizier),
    ('tfidf', tfidf ),
    ('scale', scaler),
    ('log', classifier)
    ])

params = {
    #"vect__lowercase": [False],
    "vect__stop_words": [german_stop_words],
    "scale__with_mean": [False],
    "log__max_iter": [3000],
    "log__solver": ['sag', 'saga'] #, 'lbfgs', 'saga'
    #"log__C": [1], #0.001, 0.01, 0.1, 
    #"log__multi_class": ['multinomial'] #'auto', 
    }

clf = GridSearchCV(pipe, param_grid = params, cv = kf )

print('jetzt wird gefittet')


clf.fit(X, y)

print('jetzt wird predicted')

y_pred = cross_val_predict(clf, X, y)

print('Report für: ')

print(' ')

print(classification_report(y, y_pred))

print(clf.best_params_)

print(datetime.now() - startTime)

