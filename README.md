# blockchain-for-data

Python-Project

This project establishes a blockchain that is meant to store big data files. All blockchains that I found cannot store data files like videos with several MB or even GB. This blockchain, which I call data-blockchain, is able (or will be able) to do that. 

There are two problems to solve here: a) create the data-blockchain itself and b) create a distribution method based on peer-to-peer.

First I downloaded a simple blockchain in Python from github. This sourcecode can be found in the branch "original blockchain program".

Then I changed this program and added the possibility to manage very big data files. The basic idea is simple: I use the hash commando to create a hash-value of the very big data file. The hash algorithm does that no matter how big the file is. Then I store this hash-value in the blockchain together with the name of the file, author and some more data. 

The big data file must be in the same directory as the data-blockchain.

What do I have now? There is no way that someone can change a single bit of the big data file and get the same hash-value. This is not possible. So only this specific data file generates the hash-value and only this hash-value is stored in the blockchain by producting another hash-value. So nothing can be changed. Not the file name, not the authors name, nothing. 

The production of the "double" hash code can be done at anytime to prove, that this big data file with this content was written by the author in the blockchain. 

As a result of this, noone can make a copy of the big data file a claim the content of the file as his own content. Of course you can make a copy but I can always proof, that my file was earlier than yours and that I am the owner of the data and all the ideas that are written down in this file. 

Of course the blockchain must be distributed as much as possible to create a publicity.


