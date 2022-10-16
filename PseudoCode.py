'''
def Xml_to_Dataframe(Liste Pressetexte.xml):
    
    für jedes xml-File:
        wenn eine Präsentationsform vorhanden ist:
            und wenn alle relevanten Feature vorhanden sind:
                speichere in Dataframe
            wenn nicht:
                überspringe das xml-File
    speichere erstellten Dataframe als File

def Tokenize(Liste Pressetexte.pkl):

    öffne Dataframe von File
    für jeden Text in Dataframe:
        teile Text in Sätze
        für jeden Satz:
            teile Satz in Wörter
            (stemme Wörter)
        Wörter und Sätze wieder zu Text zusammensetzen
        entferne Stoppwörter
    speichere aktualisierten Dataframe als File

def Classify_Text(Liste tokenisierter Pressetexte.pkl):
    
    [optional] nur bestimmte Pformen oder verschiedene Sample-Größen [optional]

    lade Präsentationsformen aus Datei in Variable Y 
    lade Feautre (Volltext) aus Datein in Variable X

    Initialisierung von Klassifikationspipeline
        Vectorizier
        Scaler
        Classifier

    Initialisierung der Parameterliste für die Pipeline-Komponenten

    Training des Classifiers mit KFold-Validierung und GridSearchCV
    Ausgabe der optimalen Parameter

    Vorhersage auf Testdatensatz
    Ausgabe von Konfusionsmatrix und Classification-Report


    

    



    










'''