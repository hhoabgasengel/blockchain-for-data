from blockKlasse import *
from blockchainKlasse import *
import pickle


# Neue leere Blockchain kreieren
bc = Blockchain()



while True:
    try:
        dateiname = "GenesisDokument.pdf"
        autor = "Hans-Jürgen Wochian"
        titel = "Genesis Dokument zum Start der Science 5 Blockchain"
        name = "Erstes Dokument"

        f = open(dateiname, "rb")
        dateiInhalt = f.read()
        h = hashlib.sha256()
        h.update(dateiInhalt)
        hexer = h.hexdigest()
        print (hexer)
        break
    except:
        print ("Falscher Dateiname oder Datei nicht gefunden")

genBlock = Block(name, hexer, autor, titel, dateiname)


while True:
    try:
        # Neuen Block auf Platte schreiben
        f = open("Block0", "wb")
        pickle.dump(genBlock, f)
        f.close()
        print ("Block auf Platte geschrieben")
        break
    except:
        print ("Konnte Block aus irgendeinem Grund nicht schreiben")
