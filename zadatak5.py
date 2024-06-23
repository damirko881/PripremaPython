'''
Robot se kreće po točkama pravokutnog koordinatnog sustava u ravnini, počevši od
točke (5, 7). Zadana je njegova putanja kao string sastavljen od znakova (npr: „SJIJI“)
 S (idi sjeverno),
 J (idi južno),
 I (idi istočno)
 Z (idi zapadno)
Ako korisnik unese S robot će ići na Sjever za 3 točke, a za sve ostale će ići po jednu
točku. Na primjer, ako je robot u točki (0, 0) nakon naredbe Z putuje u točku (-1, 0), a
nakon S putuje u točku (0,3). Napišite program koji određuje konačnu poziciju robota za
proizvoljan broj točaka 
'''

x = 5
y = 7

komanda = input("Unesite putanju: ")

def kretanje(komanda):
    global x, y
    for slovo in komanda:
        if slovo == 'S':
            y += 3
        elif slovo == 'J':
            y -= 1
        elif slovo == 'Z':
            x -= 1
        elif slovo == 'I':
            x += 1
        else:
            print("Pogresna komanda")

kretanje(komanda)
print("Trenutne koordinate su ($x, $y):", x, y)