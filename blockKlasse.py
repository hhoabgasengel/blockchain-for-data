import datetime
import hashlib


class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()
    hashDaten = 0x0
    Autor = None
    Titel = None
    Dateiname = ""


    def __init__(self, data, hexer, autor, titel, dateiname):
        self.data = data
        self.hashDaten = hexer
        self.Autor = autor
        self.Titel = titel
        self.Dateiname = dateiname

    def hash(self):
        h = hashlib.sha256()

        h.update(
        str(self.Dateiname).encode('utf-8') +
        str(self.nonce).encode('utf-8') +
        str(self.hashDaten).encode('utf-8') +
        str(self.Autor).encode('utf-8') +
        str(self.Titel).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        r =     "\n Dateiname: " + str(self.Dateiname)
        r = r + "\n Titel: " + str(self.Titel)
        r = r + "\n Autor: " + str(self.Autor)
        r = r + "\n Name: " + str(self.data)
        r = r + "\n Blocknummer: " + str(self.blockNo)
        r = r + "\n Hashwert der eingelagerten Daten: " + str(self.hashDaten)
        r = r + "\n Hash des aktuellen Blocks: " + str(self.hash())
        r = r + "\n Hash des vorangehenden Blocks: " + str(self.previous_hash)
        r = r + "\n--------------"
        
        return r

