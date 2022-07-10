

class Blockchain:

    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)
    aktBlock = None
    head = None

    def add(self, neuBlock):

        # Der neue Block bekommt den Hash des aktuellen Blocks eingetragen
        neuBlock.previous_hash = self.aktBlock.hash()
        
        # Der neue Block bekommt eine um 1 hoehere Nummer als der aktuelle Block
        neuBlock.blockNo = self.aktBlock.blockNo + 1

        # Der aktuelle Block zeigt auf den neuen Block
        self.aktBlock.next = neuBlock

        # Der neue Block ist der neue aktuelle Block, den die Blockchain als
        # Variable aktBlock immer mitfuehrt.
        self.aktBlock = neuBlock

    def mine(self, suchBlock):
        for n in range(self.maxNonce):
            if int(suchBlock.hash(), 16) <= self.target:
                self.add(suchBlock)
                print(suchBlock)
                break
            else:
                suchBlock.nonce += 1
