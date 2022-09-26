import nltk
from nltk import pos_tag, sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
import json, csv, pandas as pd 
import glob
import numpy as np
import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
from germalemma import GermaLemma

########################## Funktionen

# POS-Tagging
def TagPOS_Text(text_list):
    pos_list = []
    for row in text_list:
        new_row = row.split(' ')
        tagged_sent = tagger.tag(new_row)
        pos_list.append(tagged_sent)
    return pos_list

# Lemmatisierung
def lemmatizeText(text_list):
    lemmatized = []
    for lists in text_list:
        lemmasOF = []
        for tuples in lists:
            try:
                lemma = lemmatizer.find_lemma(tuples[0], tuples[1])
                lemmasOF.append(lemma)
            except ValueError:
                lemmasOF.append(tuples[0])
                continue
        lemmatized.append(" ".join(lemmasOF))
    return lemmatized

# Tokenisierung
def tokenizeText(text_list):

    stripped = []
    stemmed = []

    # Initialisiert Snowballstemmer
    stemmer = SnowballStemmer('german')

    for sendung in text_list:

        sent_of_sendung = []
        stem_of_sendung = []

        # Zerlegt jeden Text in Sätze
        tok_sentences = sent_tokenize(sendung, language='german')

        # Tokenisiert jedes Wort in jedem Satz
        for satz in tok_sentences:

            # Tokenisierung
            words = word_tokenize(satz)

            # Strip Satzzeichen
            new_words= [word for word in words if word.isalnum()]
            
            # Joined tokenisierte Wörter jedes Satzes einer Sendung
            sent_of_sendung.append(" ".join(new_words))

            # Stemming
            stemmed_words = [stemmer.stem(word) for word in new_words]
            stem_of_sendung.append(" ".join(stemmed_words))
            
        # Joined tokensierte Sätze einer Sendung
        stripped.append(" ".join(sent_of_sendung))

        # Joined gestemmte Sätze einer Sendung
        stemmed.append(" ".join(stem_of_sendung))
   
    return [
        stripped,
        stemmed
    ]

# Öffnet trainierten Korpus zum POS-Tagging    
with open('./nltk_german_classifier_data.pickle', 'rb') as f:
    tagger = pickle.load(f)

# Einstellungen für einzelne Dokumente
in_path = '../zdf_data/cleaned/csv/03_09/'
out_path = '../zdf_data/cleaned/csv/03_09/transformed/'
file = '03_09_zdf_dokumentation_'

# Einstellung um alle Dokumente zu mergen
data = pd.concat([pd.read_csv(f, encoding='utf-8', sep=';') for f in glob.glob(in_path + "/*.csv")],
                      ignore_index=True)

# Liste der Dateinamen
files = [
    '37-grad',
    'der-haustier-check',
    'dokumentation-sonstige',
    'planet-e',
    'terra-x',
    'zdf-history',
    'zdfinfo-doku',
    'zdf-reportage',
    'zdfzeit',
    'zdfzoom',
]

# Ausführung des Codes für jeden Namen in der Liste
# For-Schleife entfernen für Ausführung der gemergten Daten

for file in files:

    data = pd.read_csv(in_path + file + name + '.csv', sep=';', encoding='utf-8')

    text = data['text']

    # Tokenisierung 
    transformed_text = tokenizeText(text)

    # Fügt Dataframe Spalten hinzu
    data['stripped'] = transformed_text[0]
    data['stemmed'] = transformed_text[1]

    print('Tokenized')


    ############################ POS-Tagging

    pos = TagPOS_Text(transformed_text[0])

    # Fügt Dataframe Spalten hinzu
    #data['tagged'] = pos (ACHTUNG: LANGE SÄTZE SCHRÄNKEN DIE SPEICHERUNG EIN)

    ############################ Lemmatisierung
    lemmatizer = GermaLemma()

    lemmatized = lemmatizeText(pos)

    # Fügt Dataframe Spalten hinzu
    data['lemma'] = lemmatized

    data.to_csv(in_path + file + '_transformed_' + 'allDocs' '.csv', encoding = 'utf-8-sig', index=False, sep=";")

    print('done')
