import pickle
from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
from germalemma import GermaLemma
import nltk
from nltk import pos_tag, sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
import json, csv, pandas as pd 
import glob
import numpy as np

with open('./nltk_german_classifier_data.pickle', 'rb') as f:
    tagger = pickle.load(f)

in_path = '../zdf_data/cleaned/csv/03_09/transformed/'
filename = 'transformed_03_09_zdf_dokumentation_der-haustier-check'

data = pd.read_csv(in_path + filename + '.csv', sep=';', encoding='utf-8')

text = data['text']

def TagPOS_Text(text_list):
    pos_list = []
    for row in text_list:
        new_row = row.split(' ')
        tagged_sent = tagger.tag(new_row)
        pos_list.append(tagged_sent)
    return pos_list

pos = TagPOS_Text(text)

lemmatizer = GermaLemma()

for tuples in pos:
    print(tuples)
    break

lemmatizer.find_lemma('Tests', 'NN')
