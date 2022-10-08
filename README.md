# To Dos

1. Daten vorbereiten (Daten suchen, Feature bestimmen, neu zusammen legen)
2. Was vrauch ich für ein Eingangsformat? (Eine Spalte Text, eine Klasse, andere Infos erstmal vernachlassbar)
3. Als nächstes Modell trainieren lassen df
4. Ergebnisse Bingo




## 18.09.2022

Immer noch am rumprobieren mit welchen Funktionen ich den gewünschten Output bekomme. Momentan besteht das Problem darin, dass unter einem Tag sich noch mehrere Child-Eles befinden. Dadurch bekomme ich keine saubere Trennung so einfach her wie ich dachte. Ich muss für jedes Child-Ele eine weitere Spalte im PD einfügen, damit das reibungslos klappt. 

## 19.09.2022

Mittlerweile können mehrere Daten geladen und in Dataframe zum Training gepeichert werden. Aktuell besteht das große Problem darin, dass die Daten nicht konsistent sind. 
In den nächsten Schritten müssen die Daten oder die Fehler bereinigt werden. Fehler könnten mit Exception Handeling gekonntert werden. Schöner wäre eine saubere Liste zu haben. Problem ist, dass ich dieses Mal Fehler nicht aus den CSV Daten rausschmeißen kann. Ich muss die Exceptions on the fly handeln oder die XML Daten korrigieren, in dem ich Fehler überschreibe und die Datei erneut abspeichere. Am wichtigsten ist, dass für jede Datei minds. eine Präsentationsform vorhanden ist.

## 25.09.2022

Ich checke nun, welche unique Values die Präsentationsformen besitzen. In meinem Testdatenset sind es folgende:

   Pform  Anzahl
## 0    ESS (Essay)                                36
1    BER (Bericht)                              1413
# 2    KOM (Kommentar)                            56
## 3    REP (Reportage)                            8
## 4    REZ (Rezension)                            58
5    TIT (Titelgeschichte)                      22
# 6    INT (Interview)                            145
7    SER (Serie)                                21
# 8    GRF (Grafik?)                              81
9    LES (Leserbrief)                           5
## 10   CHR (Chronologie)                          2
11   KTE (Karte)                                8
12   PRM (Pressemitteilung)                     6
13   OFB (Offener Brief)                        1
14   SDK (Sonderdokument)                       4
15   ANA (Analysis nur für DW)                  1
16   WRT (Wortlaut)                             7
17   LEX (Lexikalisches Begriffserklärung)      1

Es fehlt noch 
# Nachruf
# Porträt/Portrait


Neuer Herausforderung: 

Not well formed XML ignorieren oder finden und ausbessern.

# 26.09.2022

Trainingsdauer muss auch gemessen werden für POC.

Problem von gester gefixed. Korrupte Files werden einfach ignoriert.

Es gibt für jeden Haupttitel auch einen Text, aber manchmal mehr als eine Pform
Es gibt nicht für jedes File einen Seitentitel oder Sonstigen Titel
Der Klassifier müsste manche Feature nur dann verwenden, wenn sie auch da sind. Fehlt ein Feature ignoriert er sie.

Umgang mit mehr als einer Pform: Wenn mehr als eine vorhanden, nimm nur erste fürs Trainings. Damit sollte kein Fehler mehr auftauchen.

Immer nur ein Ding aus Präsentationsform liste nehmen oder wenn mehr als eine vergeben, dann text und titel von der pform kopieren und ebenfalls fürs Training benutzen.

# 27.09.2022
Problem gelöst indem wir zusätzlich in der for-Schleife einen index angeben, nachdem ich dann filtern kann. ALso nur den ersten nehmen z.B.

findall vs iter
findall findet nur Element mit dem Tag, die direkte Kinder vom ausgewählten element sind
iter geht auch weiter als iter

checke ob datei x,y,z hat und nur dann mitnehmen. Nicht einzeln voneinander checken

Late Night Thoughts: 

Immer nur die erste Pform zu nehmen könnte dazu führen, dass sehr wenig Trainingsmaterial übrig bleibt. Stichprobe zeigt, dass z.B. das Tag "GRF" sehr häufig nur als zweite Pform kommt. Vermutlich weil Bestandteil des Artikels, aber nicht nur der Artikel. Dennoch interessant für die Recherche, weil mit Stichwörtern das Thema eingeschränkt werden kann und mit den Pform = Grafik eine Schaubild passend zum Thema gesucht werden kann.

# 28.09.2022

Heute läuft irgendwie gar nix. Mehrmals rumprobiert aber ich konnte das Problem nach wie vor nicht lösen. Im Netz wird immer nur vorgeschlagen, dass man die korrputen Files bearbeitet, mir ist bei einem Testlauf aber aufgefallen, dass immer die letzte Datei als korrupt angezeigt wird.

# 29.09.2022

Endlich das Problem gefixt. Nun werden Dateien ignoriert, die entweder keine pform, kein Titel oder Text beinhalten.
Auf alle Daten angewendet kommen am Ende <b>1.472.129</b> Files zum Training infrage.
Nur mit Pforms aus den Prios 1 und 2: sind es noch <b>354.907</b>

Für jede Klasse bleiben:
INT    115.759
REZ    101.473
GRF     55.767
KOM     53.888
REP     13.584
ESS     12.056
CHR      2.380

Subsample-Größe
INT    32769
REZ    28492
GRF    15862
KOM    15117
REP     3771
ESS     3324
CHR      665


morgen hier lesen:
 https://scikit-learn.org/stable/modules/preprocessing.html
 C:\Users\tschu\anaconda3\lib\site-packages\sklearn\linear_model\_logistic.py:762: ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(


# 01.10.2022

0:50:46.855603

Zeit die es braucht um XML in Dataframe umzuwandeln, und anschließend 

Tokenized
1:31:13.544934

# 03.10.2022
https://www.section.io/engineering-education/classification-model-using-bert-and-tensorflow/

              precision    recall  f1-score   support

         CHR       0.01      0.07      0.02        60
         ESS       0.11      0.26      0.16       337
         GRF       0.48      0.59      0.53      1619
         INT       0.72      0.67      0.69      3281
         KOM       0.56      0.33      0.42      1513
         REP       0.16      0.42      0.23       359
         REZ       0.79      0.58      0.67      2831

    accuracy                           0.55     10000
   macro avg       0.41      0.42      0.39     10000
weighted avg       0.63      0.55      0.58     10000

Ergebnisse aus der SGD

Ich muss vielleicht ein Modell für jede Klasse morgen ausprobieren. Dat wird doch sonst nix hier.

              precision    recall  f1-score   support

         CHR       0.00      0.00      0.00        60
         ESS       0.60      0.01      0.02       337
         GRF       0.74      0.74      0.74      1619
         INT       0.60      0.95      0.74      3281
         KOM       0.70      0.17      0.27      1513
         REP       1.00      0.01      0.01       359
         REZ       0.89      0.89      0.89      2831

    accuracy                           0.71     10000
   macro avg       0.65      0.39      0.38     10000
weighted avg       0.73      0.71      0.66     10000

Ergebnisse mit Naivem Bayes



             precision    recall  f1-score   support

         CHR       0.00      0.00      0.00        23
         ESS       0.67      0.01      0.02       183
         GRF       0.78      0.83      0.81       791
         INT       0.90      0.92      0.91      1612
         KOM       0.71      0.78      0.74       756
         REP       0.82      0.42      0.56       193
         REZ       0.86      0.95      0.90      1442

    accuracy                           0.84      5000
   macro avg       0.68      0.56      0.56      5000
weighted avg       0.83      0.84      0.82      5000

Ergebnisse SVM mit sigmoid



Ergebnisse sgd Log

scaler__with_mean': False, 'sgd__alpha': 0.1, 'sgd__loss': 'log', 'sgd__max_iter': 5000, 'vect__lowercase': False, 'vect__stop_words'

              precision    recall  f1-score   support

         CHR       0.00      0.00      0.00        60
         ESS       0.10      0.14      0.12       337
         GRF       0.56      0.64      0.60      1619
         INT       0.70      0.79      0.74      3281
         KOM       0.64      0.37      0.47      1513
         REP       0.19      0.28      0.22       359
         REZ       0.80      0.71      0.75      2831

    accuracy                           0.63     10000
   macro avg       0.43      0.42      0.41     10000
weighted avg       0.65      0.63      0.64     10000



 
              precision    recall  f1-score   support

         CHR       0.14      0.04      0.06       665
         ESS       0.24      0.08      0.11      3324
         GRF       0.76      0.80      0.78     15862
         INT       0.83      0.91      0.87     32769
         KOM       0.78      0.68      0.73     15117
         REP       0.59      0.28      0.38      3771
         REZ       0.86      0.94      0.90     28492

    accuracy                           0.81    100000
   macro avg       0.60      0.53      0.55    100000
weighted avg       0.79      0.81      0.79    100000
SGD SVM

{'scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase': False, 'vect__stop_words':



         CHR       0.63      0.65      0.64      2380
         ESS       0.58      0.62      0.60      2380
         GRF       0.67      0.68      0.67      2380
         INT       0.73      0.79      0.76      2380
         KOM       0.67      0.50      0.57      2380
         REP       0.68      0.72      0.70      2380
         REZ       0.80      0.78      0.79      2380

    accuracy                           0.68     16660
   macro avg       0.68      0.68      0.68     16660
weighted avg       0.68      0.68      0.68     16660

{'scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase': False, 'vect__stop_words':




               precision    recall  f1-score   support

         GRF       0.73      0.82      0.77      2471
         INT       0.83      0.92      0.87      5162
         KOM       0.88      0.56      0.68      2367

    accuracy                           0.81     10000
   macro avg       0.81      0.77      0.78     10000
weighted avg       0.82      0.81      0.80     10000


'scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase': False, 'vect__stop_words'


Modell saven und laden noch machbar machen. Andere Feature ausprobieren.

              precision    recall  f1-score   support

         GRF       0.80      0.83      0.82     12443
         INT       0.88      0.94      0.90     25601
         KOM       0.90      0.73      0.81     11956

    accuracy                           0.86     50000
   macro avg       0.86      0.83      0.84     50000
weighted avg       0.86      0.86      0.86     50000


{'scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase': False, 'vect__stop_words':




'scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase': False