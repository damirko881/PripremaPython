1. Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar 
liste. Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30. 
Primjer ulaza: [4, 6, 6, 6, 3, 8, 21, 21,21, 7, ...] 
Izlaz: 6, 21
-----------------------------------------------------------------------------------------------------------------------
2. Napisati Python funkciju koja filtrira vrijednosti rjecnika na osnovu visine i kao rezultat 
daje novi rjecnik. Argumenti funkcije trebaju biti rjecnik, i visina po kojoj se filtrira. 
(primjer: filtrira sve osobe koje su vece od odredene visine) 
Rjecnik: 
{'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190}
-----------------------------------------------------------------------------------------------------------------------
3. Napisi program i funkciju loto642 koja simulira loto 6/42. 
a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih 
brojeva. Funkcija vraća listu loto brojeva. 
b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno). 
c. Potrebno je odrediti ukupan broj pogodataka pri izvlačenju i ispisati na ekran. 
d. Odrediti sumu pogođenih, minimum i maksimalni pogođeni broj.
-----------------------------------------------------------------------------------------------------------------------
4. Kreirati listu prirodnih brojeva od 50 elemenata (koristiti random funkciju). Za danu 
listu prirodnih brojeva stvori rječnik u kojemu će se nalaziti frekvencija pojavljivanja 
određene brojčane znamenke u svim brojevima iz liste 
Npr. za [423, 54, 45] broj 4 se pojavljuje 3 puta, 2 - 1 put, 3 -1 put, itd 
Napomena: ključevi rječnika neka budu brojevi, a ne stringovi.
-----------------------------------------------------------------------------------------------------------------------
5. Robot se kreće po točkama pravokutnog koordinatnog sustava u ravnini, počevši od 
točke (5, 7). Zadana je njegova putanja kao string sastavljen od znakova (npr: „SJIJI“) 
 S (idi sjeverno), 
 J (idi južno), 
 I (idi istočno) 
 Z (idi zapadno) 
Ako korisnik unese S robot će ići na Sjever za 3 točke, a za sve ostale će ići po jednu 
točku. Na primjer, ako je robot u točki (0, 0) nakon naredbe Z putuje u točku (-1, 0), a 
nakon S putuje u točku (0,3). Napišite program koji određuje konačnu poziciju robota za 
proizvoljan broj točaka
-----------------------------------------------------------------------------------------------------------------------
6. Postaviti parametre kružnice (r i koordinate središta (a, i b). Zatim je potrebno učitavati 
10 točaka koordinatnog sustava (realni brojevi). 
 Za učitane točke provjeriti nalaze li se na kružnici. (25 bodova) 
 Nakon što se učita točka (0, 0), ispisati koliki je omjer pogodaka kružnice ((broj 
točaka na kružnici)/(ukupni broj točaka)) u postotku (25 bodova) 
Formula kružnice : (x-a)2+(y-b)2=r2
-----------------------------------------------------------------------------------------------------------------------
7. Za dani riječnik čiji su ključevi imena studenata, a vrijednosti ocjene. Vrijednosti trebaju 
biti u obliku ntorke. Potrebno je vratiti rječnik čiji će ključevi biti prosječna ocjena 
(zaokružena - koristiti round() funkciju),a vrijednosti sortirana lista studenata koji su 
dobili tu prosječnu ocjenu. 
Npr. u rječniku {'ivan': (3,2,4), 'marko': (5,5,4), 'ana': (2,3,4)}, 'ivan' ima ocjene 3, 2, 4 i 
prosječna ocjena je 3.0, 'marko' ima ocjene 5, 4 i prosječna ocjena je 4.0, 'ana' ima 
ocjene 2, 3, 4 i prosječna ocjena je 3.0. 
 Izlazni rječnik će biti {3: ['ana', 'ivan'], 4: ['marko']} jer 'ivan' i 'ana' imaju prosjek 3.0, a 
'marko' prosjek 4
-----------------------------------------------------------------------------------------------------------------------
8. Za danu listu stringova, vrati rječnik čiji će ključevi biti znakovi iz stringova, a vrijednosti 
lista stringova koji sadrže taj znak po redoslijedu pojavljivanja u originalnom stringu. 
Napravite vlastitu funkciju, 
Npr. za listu ['dobar','dan'] će se dobiti rječnik 
 {'d': ['dobar', 'dan'], 'o': ['dobar'],'b':['dobar'],'a':['dobar', 'dan'], 'r': ['dobar'], 'n': ['dan']}
-----------------------------------------------------------------------------------------------------------------------
9. Za danu matricu stringova pronađi elemente koji nisu brojcani stringovi i vrati rječnik čiji 
će ključ biti njihovih pozicija, a vrijednost sam element. Pozicija je predstavljena kao 
uređeni par (x,y) gdje je x broj reda, a y broj stupca elementa koji nije broj. Napravite 
vlastitu funkciju. 
Napomena: prvi redak i prvi stupac imaju poziciju 0. Npr. za matricu 
 5 4 a 1 
 c 3 12 b 
 7 9 0 d 
se dobiva {(0,2): 'a', (1,0): 'c', (1,3): 'b', (2,3): 'd'}
-----------------------------------------------------------------------------------------------------------------------
10. Za danu listu stringova vrati broj stringova iz liste kojima je duljina >=3 i koji imaju barem 
dvije znamenke jednake prvoj znamenci. 
Npr. za listu ['abc', 'aba', 'cc', 'ijki'] će vratiti 2
