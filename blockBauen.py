from tkinter import *
import datetime
import hashlib
import pickle
import os
from blockKlasse import *
from blockchainKlasse import *


#
# Globale Variablen
#
dateiname = None



# Neue leere Blockchain kreieren
bc = Blockchain()



# Genesis-Block lesen
f = open("Block0", "rb")
gblock = pickle.load(f)
f.close()
# head festlegen. Bleibt unveraendert
dummy = bc.head = gblock
# aktBlock festlegen. Wird immer einen weitergeschoben
dummy = bc.aktBlock = gblock



#
#
# HIer muss man aufpassen, dass man keinen Trojaner-Block untergeschoben bekommen hat.
# Man muss also checken, ob die im Block gespeicherten Hash-Werte immer noch mit frisch
# erzeugten Hash-Werten übereinstimmen.
#
#



lauf = 1

while True:
    try:
        f = open("Block" + str(lauf), "rb")
        eblock = pickle.load(f)
        f.close()

        # Aktuellen Block auf den neu eingelesenen Block zeigen lassen
        dummy = bc.aktBlock.next = eblock

        # Previous_hash des neuen Blockes auf Hash-Wert des aktuellen Blockes stellen
        bc.aktBlock.next.previous_hash = bc.aktBlock.hash()

        # Aktuellen Bock auf den neuen Block setzen.
        dummy = bc.aktBlock = eblock

        
        lauf = lauf + 1
    except:
        print ("Blockchain eingelesen")
        break



while True:
    try:
        dateiname = str(input("Bitte Dateiname eingeben: "))
        autor = str(input("Autor eingeben: "))
        titel = str(input("Titel eingeben: "))
        name = str(input("Blockname eingeben: "))

        f = open(dateiname, "rb")
        dateiInhalt = f.read()
        h = hashlib.sha256()
        h.update(dateiInhalt)
        hexer = h.hexdigest()
        print (hexer)
        break
    except:
        print ("Falscher Dateiname oder Datei nicht gefunden")


# Block in Kette einhaengen
bc.add(Block(name, hexer, autor, titel, dateiname))

# Dateiname fuer Block ermitteln
dname = "Block" + str(bc.aktBlock.blockNo)

while True:
    try:
        # Neuen Block auf Platte schreiben
        f = open(dname, "wb")
        pickle.dump(bc.aktBlock, f)
        f.close()
        print ("Block auf Platte geschrieben")
        break
    except:
        print ("Konnte Block aus irgendeinem Grund nicht schreiben")


        
        
