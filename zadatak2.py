'''
Napisati Python funkciju koja filtrira vrijednosti rjecnika na osnovu visine i kao rezultat
daje novi rjecnik. Argumenti funkcije trebaju biti rjecnik, i visina po kojoj se filtrira.
(primjer: filtrira sve osobe koje su vece od odredene visine)
Rjecnik:
{'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190} 
'''

rijecnik = {'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190} 

def filtriraj(rijecnik, min_visina):
    novi_rijecnik = {}
    for ime, visina in rijecnik.items():
        if visina >= min_visina:
            novi_rijecnik[ime] = visina
    
    return novi_rijecnik

test = filtriraj(rijecnik, 200)
print(test)


'''
# drugi nacin

def filtriraj(rijecnik, minimalna_visina):
    return {ime: visina for ime, visina in rijecnik.items() if visina >= minimalna_visina}

'''