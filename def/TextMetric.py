import nltk
from nltk import pos_tag, sent_tokenize, wordpunct_tokenize
import json, csv, pandas as pd 
import glob
from textblob_de import TextBlobDE as TextBlob
from textblob_de import PatternTagger
from collections import Counter
import numpy as np

path = '../zdf_data/cleaned/csv/03_09/'
file = '03_09_zdf_dokumentation_'

names = [
    '37-grad',
    'der-haustier-check',
    'dokumentation-sonstige',
    'planet-e',
    'terra-x',
    'zdf-history',
    'zdfinfo-doku',
    'zdf-reportage',
    'zdfzeit',
    'zdfzoom'
]

# Ausführung für Gesamtdaten for-Schleife entfernen
big_frame = pd.concat([pd.read_csv(f, sep=';') for f in glob.glob(path + "/*.csv")],
                      ignore_index=True)
allText = big_frame['text']

# Ausführung für jeden Datensatz in einer Schleife
for name in names:
    allDocs = pd.read_csv(path + file + name + '.csv', sep=';')
    allText = allDocs['text']

    word_list = []
    docs = []
    for row in allText:
        sente = []
        if not row:
            continue
        text = TextBlob(row)
        rows = text.sentences
        for saetze in rows:
            tokens = saetze.words
            sente.append(tokens)
            word_list.append(tokens)
        docs.append(sente)

    lengths = []
    for row in docs:
        counts = []
        for sentes in row:
            counts.append((len(sentes)))
        lengths.append(counts)

    counts_of_words = []
    for list in lengths:
        counts_of_words.append(sum(list))

    # Types und Tokens
    new = []
    counter = 0
    for list in word_list:
        for words in list:
            new.append(words)
            counter += 1
    c = Counter(new)

    print(name)
    print("Average Text: ", np.mean(counts_of_words))
    print("Median Text: ", np.median(counts_of_words))
    print("Längster Text: ", max(counts_of_words))
    print("Kürzester Text: ", min(counts_of_words))
    print("Types: ", len(c))
    print("Tokens: ", counter)
    print('--------------------------------------------------------')

"""
# Visualisierung
c_sort = c.most_common()
pandas = pd.DataFrame(c_sort, columns=['word', 'Termfrequenz'])

pandas.iloc[0:1000].plot(x='word', y='Termfrequenz', color='#FA7D19', kind='line', use_index=False)
plt.xlabel('Index der Wörter im Korpus')
plt.ylabel('Frequenz')
plt.show()
"""