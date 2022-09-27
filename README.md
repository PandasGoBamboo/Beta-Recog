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