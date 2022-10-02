import nltk
from nltk import pos_tag, sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
import pandas as pd 
import numpy as np
import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
from germalemma import GermaLemma
from datetime import datetime

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

# Counter für Dauer von Skriptausführung
startTime = datetime.now()

# Konsolenoutput
print('ich roedel....')

# Öffnet trainierten Korpus zum POS-Tagging    
with open('nltk_german_classifier_data.pkl', 'rb') as f:
    tagger = pickle.load(f)

# Einstellung um alle Dokumente zu mergen
data = pd.read_pickle('raw_data.pkl')

# select only 1000 of Data

data_to_select = data.sample(n=100000, random_state=1)

text = data_to_select['volltext']
# Tokenisierung 
transformed_text = tokenizeText(text)

 # Fügt Dataframe Spalten hinzu
data_to_select['stripped'] = transformed_text[0]
data_to_select['stemmed'] = transformed_text[1]

print('Tokenized')
data_to_select.to_pickle('stemmed-stripped_1000_raw_data.pkl')


############################ POS-Tagging

pos = TagPOS_Text(transformed_text[0])

# Fügt Dataframe Spalten hinzu
#data['tagged'] = pos (ACHTUNG: LANGE SÄTZE SCHRÄNKEN DIE SPEICHERUNG EIN)

print('tagged')
############################ Lemmatisierung
lemmatizer = GermaLemma()

lemmatized = lemmatizeText(pos)

# Fügt Dataframe Spalten hinzu
data_to_select['lemma'] = lemmatized

data_to_select.to_pickle('prepro_1000_raw_data.pkl')

print('ich habe fertig')
print(datetime.now() - startTime)

