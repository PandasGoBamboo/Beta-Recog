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





              precision    recall  f1-score   support

         CHR       0.10      0.02      0.03       121
         ESS       0.22      0.05      0.08       567
         GRF       0.60      0.42      0.50      3045
         INT       0.57      0.79      0.66      6788
         KOM       0.66      0.41      0.50      3007
         REP       0.18      0.04      0.07       692
         REZ       0.70      0.76      0.73      5780

    accuracy                           0.62     20000
   macro avg       0.43      0.35      0.37     20000
weighted avg       0.60      0.62      0.59     20000




              precision    recall  f1-score   support

         CHR       0.10      0.02      0.03       322
         ESS       0.27      0.05      0.09      1439
         GRF       0.65      0.47      0.55      7563
         INT       0.59      0.81      0.68     16779
         KOM       0.71      0.45      0.55      7679
         REP       0.23      0.05      0.09      1772
         REZ       0.73      0.80      0.76     14446

    accuracy                           0.65     50000
   macro avg       0.47      0.38      0.39     50000
weighted avg       0.63      0.65      0.62     50000

'scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'log', 'sgd__max_iter': 5000, 
on Titels






              precision    recall  f1-score   support

         CHR       0.50      0.03      0.06        66
         ESS       0.14      0.01      0.02       274
         GRF       0.67      0.48      0.56      1527
         INT       0.64      0.83      0.72      3381
         KOM       0.64      0.41      0.50      1514
         REP       0.39      0.03      0.06       348
         REZ       0.71      0.86      0.78      2890

    accuracy                           0.66     10000
   macro avg       0.53      0.38      0.38     10000
weighted avg       0.64      0.66      0.63     10000
Text und Titel



              precision    recall  f1-score   support

         CHR       0.00      0.00      0.00       322
         ESS       0.24      0.02      0.04      1439
         GRF       0.70      0.59      0.64      7563
         INT       0.71      0.84      0.77     16779
         KOM       0.66      0.54      0.59      7679
         REP       0.52      0.08      0.13      1772
         REZ       0.75      0.88      0.81     14446

    accuracy                           0.71     50000
   macro avg       0.51      0.42      0.43     50000
weighted avg       0.69      0.71      0.69     50000
Text und Titel

              precision    recall  f1-score   support

         GRF       0.76      0.63      0.69     11921
         INT       0.79      0.93      0.85     26142
         KOM       0.79      0.63      0.70     11937

    accuracy                           0.79     50000
   macro avg       0.78      0.73      0.75     50000
weighted avg       0.78      0.79      0.78     50000
Text Titel nur grf. int. komm

              precision    recall  f1-score   support

         CHR       0.05      0.01      0.01       322
         ESS       0.17      0.01      0.02      1439
         GRF       0.74      0.68      0.71      7563
         INT       0.79      0.87      0.83     16779
         KOM       0.67      0.61      0.64      7679
         REP       0.60      0.13      0.21      1772
         REZ       0.79      0.94      0.86     14446

    accuracy                           0.77     50000
   macro avg       0.55      0.46      0.47     50000
weighted avg       0.74      0.77      0.74     50000
nur die ersten 300

Welche Tests habe ich durchgeführt?

1. Mit und ohne Stoppwortliste
2. Auf Erfahrungen basierend nur mit gestrippten Texten gearbeitet. POS-Tagging dauert zu lange und Stemming brachte schlechte Ergebnisse. Wenn nötig einfach faken, dass ich das getestet habe
3. Verschiedene Trainingsmengen. 5000 bis 100.000 Dokumente. Es zeigte sich grob gesagt: je mehr desto besser, mindestens scheinen 5k Dokumente benötigt zu werden.
4. Verschiedene Klassifikatoren. Meistens aber SGD-SVM (linear) oder Logistische Regression. SGD linear SVM am effizientesten.
5. Verschiedene Klassengrößen. Nur mit den frequentesten oder nur mit den infrequentesten.
6. Mit Titeln und Seitentiteln, plus ersten 100 bzw. 300 Wörter
7. Nur die ersten 100 - 300 Wörter

# Visualierungen

1. Zeitstrahl um zu zeigen wie lange das gedauert hat
2. Kuchendiagramm mit und ohne Prio 1/2 Präsentationsformen
3. Precision Recall Matrix
4. Pseudo-Code
5. 


              precision    recall  f1-score   support

         ANA       0.00      0.00      0.00         6
         BER       0.76      0.96      0.85      3669
         CHR       0.00      0.00      0.00         7
         ESS       0.00      0.00      0.00        36
         FRG       0.00      0.00      0.00         1
         GRF       0.26      0.05      0.08       174
         INT       0.44      0.13      0.20       423
         KOM       0.50      0.02      0.04       159
         KTE       0.00      0.00      0.00        22
         LES       0.00      0.00      0.00         1
         LEX       0.00      0.00      0.00         2
         PRM       0.00      0.00      0.00        16
         REP       0.00      0.00      0.00        40
         REZ       0.68      0.21      0.32       346
         SAT       0.00      0.00      0.00         1
         SER       0.04      0.02      0.03        51
         TIT       0.00      0.00      0.00        37
         WRT       0.00      0.00      0.00         9

    accuracy                           0.73      5000
   macro avg       0.15      0.08      0.08      5000
weighted avg       0.66      0.73      0.66      5000


Max Feature stehen auf 1500 häufigsten Wörter. Könnte man natürlich noch erhöhen.
Stellschrauben, Verhähltnisse Matrialien. 

In EG Mining vorstellen. In Presse vorstellen. Richtung Team Mining Ralph Walhöfer vorstellen. Ihre Einschätzung dazu.

[[   75    17   705   481   261    99   254]
 [   12   625   467  1474  3895   178  2112]
 [   89   185 36234  4630  2319   530  1188]
 [  100   205  3085 92527  1156   453  2232]
 [   87   591  2619  4117 35477   351  2870]
 [   28   117  1407  2229  1011  3545  2214]
 [   70   408   608  2006  1244   464 81159]]
 
 scaler__with_mean': False, 'sgd__alpha': 1.0, 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase'

               precision    recall  f1-score   support

         CHR       0.16      0.04      0.06      1892
         ESS       0.29      0.07      0.11      8763
         GRF       0.80      0.80      0.80     45175
         INT       0.86      0.93      0.89     99758
         KOM       0.78      0.77      0.78     46112
         REP       0.63      0.34      0.44     10551
         REZ       0.88      0.94      0.91     85959

    accuracy                           0.84    298210
   macro avg       0.63      0.56      0.57    298210
weighted avg       0.82      0.84      0.82    298210
2022-10-14 15:21:53.396902
-1 day, 19:46:55.724696


Report für: stripped

[[   76    18   704   480   266    99   249]
 [   12   621   478  1445  3922   182  2103]
 [   94   193 36266  4610  2316   525  1171]
 [  103   199  3095 92470  1164   461  2266]
 [   90   589  2627  4108 35466   366  2866]
 [   32   116  1406  2219   998  3571  2209]
 [   77   419   606  1994  1236   464 81163]]

               precision    recall  f1-score   support

         CHR       0.16      0.04      0.06      1892
         ESS       0.29      0.07      0.11      8763
         GRF       0.80      0.80      0.80     45175
         INT       0.86      0.93      0.89     99758
         KOM       0.78      0.77      0.78     46112
         REP       0.63      0.34      0.44     10551
         REZ       0.88      0.94      0.91     85959

    accuracy                           0.84    298210
   macro avg       0.63      0.56      0.57    298210
weighted avg       0.82      0.84      0.82    298210

Mit anderer Stoppwortliste

Report für: stripped

[[   77    16   724   490   243   101   241]
 [   13   638   483  1488  3864   181  2096]
 [   94   201 36381  4643  2177   527  1152]
 [  116   202  3104 92601  1086   470  2179]
 [   96   606  2518  4130 35602   354  2806]
 [   31   125  1445  2283   972  3535  2160]
 [   64   420   595  2015  1147   500 81218]]

 unprozessierte Texte

               precision    recall  f1-score   support

         CHR       0.16      0.04      0.06      1892
         ESS       0.29      0.07      0.12      8763
         GRF       0.80      0.81      0.80     45175
         INT       0.86      0.93      0.89     99758
         KOM       0.79      0.77      0.78     46112
         REP       0.62      0.34      0.44     10551
         REZ       0.88      0.94      0.91     85959

    accuracy                           0.84    298210
   macro avg       0.63      0.56      0.57    298210
weighted avg       0.82      0.84      0.82    298210
2022-10-15 14:50:55.004688
-1 day, 18:02:26.571392



SVC mit 5k Daten
'scaler__with_mean': False, 'sgd__C': 1.0, 'sgd__class_weight': 'balanced', 'sgd__kernel': 'sigmoid', 'sgd__max_iter': 5000, 'vect__lowercase':
              precision    recall  f1-score   support

         CHR       0.00      0.00      0.00        41
         ESS       0.20      0.01      0.01       132
         GRF       0.63      0.74      0.68       744
         INT       0.67      0.84      0.75      1706
         KOM       0.79      0.18      0.29       758
         REP       0.60      0.03      0.07       173
         REZ       0.76      0.95      0.85      1446

    accuracy                           0.70      5000
   macro avg       0.52      0.39      0.38      5000
weighted avg       0.69      0.70      0.65      5000

-1 day, 11:09:53.224965

{'scaler__with_mean': False, 'sgd__class_weight': 'balanced', 'sgd__loss': 'hinge', 'sgd__max_iter': 5000, 'vect__lowercase': False, 'v

          precision    recall  f1-score   support

         CHR       0.05      0.59      0.09      1892
         ESS       0.12      0.39      0.19      8763
         GRF       0.63      0.61      0.62     45175
         INT       0.84      0.69      0.76     99758
         KOM       0.72      0.50      0.59     46112
         REP       0.21      0.51      0.29     10551
         REZ       0.88      0.66      0.75     85959
         
    accuracy                           0.62    298210
   macro avg       0.49      0.56      0.47    298210
weighted avg       0.75      0.62      0.67    298210
2022-10-19 09:28:40.645255
-1 day, 14:28:32.574536

NAIVE BAYES ALLE DATEN

Report für: stripped

[[  301    49   419   630   185   185   123]
 [  115  1867   837  2053  1514   426  1951]
 [  848   869 30194  8905  2024  1412   923]
 [ 1520  3044 15108 59661  5261  3971 11193]
 [  670  3288  6848 11101 18936  1524  3745]
 [  314   314  1017  2307   776  4387  1436]
 [  908  3114  1789  8483  1559  2906 67200]]
 


              precision    recall  f1-score   support

         CHR       0.06      0.16      0.09      1892
         ESS       0.15      0.21      0.18      8763
         GRF       0.54      0.67      0.60     45175
         INT       0.64      0.60      0.62     99758
         KOM       0.63      0.41      0.50     46112
         REP       0.30      0.42      0.35     10551
         REZ       0.78      0.78      0.78     85959

    accuracy                           0.61    298210
   macro avg       0.44      0.46      0.44    298210
weighted avg       0.63      0.61      0.62    298210
2022-10-23 10:14:36.933877
-1 day, 20:00:59.234095