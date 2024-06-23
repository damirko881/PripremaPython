'''
Za danu listu stringova vrati broj stringova iz liste kojima je duljina >=3 i koji imaju barem
dvije znamenke jednake prvoj znamenci.
Npr. za listu ['abc', 'aba', 'cc', 'ijki'] će vratiti 2 
'''

lista =  ['abc', 'aba', 'cc', 'ijki']

brojac = 0
for word in lista:
    flag = False
    pocetno_slovo = word[0]
    if len(word) >= 3:
        for slovo in word[1:]:
            if pocetno_slovo == slovo:
                flag = True
        if flag == True:
            brojac += 1

print(brojac)