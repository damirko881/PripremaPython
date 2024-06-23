'''
Kreirati listu prirodnih brojeva od 50 elemenata (koristiti random funkciju). Za danu
listu prirodnih brojeva stvori rječnik u kojemu će se nalaziti frekvencija pojavljivanja
određene brojčane znamenke u svim brojevima iz liste
Npr. za [423, 54, 45] broj 4 se pojavljuje 3 puta, 2 - 1 put, 3 -1 put, itd
Napomena: ključevi rječnika neka budu brojevi, a ne stringovi. 
'''

import random

lista = []
for i in range(50):
    broj = random.randint(1,1000)
    lista.append(broj)

frekvencija_znamenki = {i: 0 for i in range(10)}

for broj in lista:
    for znamenka in str(broj):
        frekvencija_znamenki[int(znamenka)] += 1

print(frekvencija_znamenki)