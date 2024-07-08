#napisati program koji ucitava prirodni broj s 8 znamenki i i ispisuje zbroj njegovih znamenki ako su neparne i djeljive sa 3

broj = input("Unesite prirodni broj s 8 znamenki: ")

if len(broj) != 8 or not broj.isdigit():
    print("Uneseni broj nije ispravan. Unesite broj s 8 znamenki.")
else:
    zbroj = 0
    for znamenka in broj:
        znamenka = int(znamenka)
        if znamenka % 2 != 0 and znamenka % 3 == 0:
            zbroj += znamenka

    print("Zbroj znamenki koje su neparne i djeljive s 3 je:", zbroj)
