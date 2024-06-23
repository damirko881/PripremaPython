'''
Napisi program i funkciju loto642 koja simulira loto 6/42.
a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih
brojeva. Funkcija vraća listu loto brojeva.
b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno).
c. Potrebno je odrediti ukupan broj pogodataka pri izvlačenju i ispisati na ekran.
d. Odrediti sumu pogođenih, minimum i maksimalni pogođeni broj. 
'''
import random

moji_brojevi = []

for i in range(6):
    moji_brojevi.append(int(input("Unesite brojeve: ")))

print(moji_brojevi)



def loto642(lista):
    max = 0
    min = 43
    suma = 0
    loto_brojevi = []
    pogodjeni_brojevi = 0
    for broj in range(6):
        lotoBroj = random.randint(1,42)
        loto_brojevi.append(lotoBroj)

        for i in lista:
            if i == lotoBroj:

                pogodjeni_brojevi += 1
                suma += lotoBroj

                if lotoBroj > max:
                    max = lotoBroj

                if lotoBroj < min:
                    min = lotoBroj 
    print("loto brojevi: ", loto_brojevi)
    print("Pogodili ste ", pogodjeni_brojevi, "brojeva")
    print("max: ", max)
    print("min: ", min)
    print("suma: ", suma)

loto642(moji_brojevi)