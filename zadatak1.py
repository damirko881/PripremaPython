'''
Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar
liste. Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30.
Primjer ulaza: [4, 6, 6, 6, 3, 8, 21, 21,21, 7, ...]
Izlaz: 6, 21 
'''

import random

lista = []
for i in range(0, 100):
    lista.append(random.randint(0,30))

brojaci = {}
counter = 1
for i in lista:
    if i in brojaci:
        brojaci[i] += 1
    else:
        brojaci[i] = 1

ponavljajuci = [x for x, brojac in brojaci.items() if brojac >= 3]
print(lista)
print("Ponavljajuca")
print(ponavljajuci)