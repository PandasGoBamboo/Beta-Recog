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
from sklearn.linear_model import LogisticRegression, SGDClassifier, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV, KFold, ShuffleSplit


############################ Datei laden
all = pickle.load(open("allDocs.p", "rb"))
all2 = pickle.load(open("allDocs_to_classify.p", "rb"))

path = '../zdf_data/cleaned/csv/03_09/'
all = pd.read_csv(path + '03_09_zdf_dokumentation__transformed_allDocs.csv', encoding='utf-8', sep=';')

lemma_file = pd.read_csv(path + 'lemmatestframe.csv', encoding='utf-8', sep=';')
lemma = lemma_file['lemma']

all['lemma'] = lemma
# Spalte, die zum Training verwendet wird

all_prePro = [
    'stripped',
    'stemmed',
    'lemma'
    ]

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

X = all['stripped']
y = all['brand']

# Vektorisierungsmethode 
vectorizier = CountVectorizer(lowercase=False, stop_words=german_stop_words, binary=True)

# Scaler
scaler = StandardScaler(with_mean=False)

tfidf = TfidfTransformer()

# Klassifikator
classifier = LogisticRegression(max_iter=2000, C=1, solver='lbfgs') 
kf = KFold(n_splits=10, shuffle=True, random_state=42)

pipe = Pipeline([
    ('vect', vectorizier),
    ('tfidf', tfidf),
    ('scale', scaler),
    ('log', classifier)
    ])

pipe.fit(X, y)

y_pred = cross_val_predict(pipe, X, y, cv=kf)

print(classification_report(y, y_pred))

# Liste der Labels


"""
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

############################ Vektorisierung
cv = CountVectorizer()
cv.fit(X_train)

X_train = cv.transform(X_train)
X_test = cv.transform(X_test)

############################ Klassifikation
    
clf = LogisticRegression(max_iter=500)
scaler = StandardScaler(with_mean=False)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred))
print('--------------------------------------------------------------------------')

# Logistische Regression
"""

"""


    # Naiver Bayes

    mNB = MultinomialNB()
    mNB.fit(X_train, y_train)
    y_pred = mNB.predict(X_test)


    print('accuracy %s' % accuracy_score(y_pred, y_test))
    print(classification_report(y_test, y_pred))
    print('--------------------------------------------------------------------------')

# Support Vektor Maschine

svm = SGDClassifier()
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

############################ Output der Confusionsmatrix
print('accuracy %s' % accuracy_score(y_pred, y_test))
print(classification_report(y_test, y_pred))

classifier = [
    MultinomialNB(),
    LogisticRegression(max_iter=200),
    SGDClassifier()
]
"""