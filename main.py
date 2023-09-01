#f(x,y,z) = 2x+4y -z
#f(2) = 2 * 2 + 4

#f(-5) = 2 *-5 +4

def replaceAll(ciag, znaki, zamiana):
    ciagret = ''
    for znak in ciag:
        #for znspec in znaki:
        #    if znak == znspec: break
        #else:
        #    ciagret += znak
        if znak not in znaki: ciagret += znak
        else: ciagret += zamiana
    return ciagret

zdanie = "Ala ma kota, kot ma Alę."
#zdanie = input("Wpisz dowolną frazę: ")

spec = (',', '.', ' ', '!', '@')
for slowo in zdanie.split(" "):
    print(len(replaceAll(slowo, spec, '')), end=" ")
print(end="\n")
zn_spec = 0
zn_spec_spacja = 0



for znak in zdanie:
    if znak in spec:
        if znak != ' ':
            zn_spec+=1
        zn_spec_spacja += 1
    #if znak in spec:
    #    zn_spec_spacja+=1
    #for zn in spec:
    #    if znak == zn and zn!=" ": zn_spec+=1
    #    if znak == zn: zn_spec_spacja+=1

print(zn_spec, "(licząc spacje", zn_spec_spacja,")")
    #if znak in spec:

znaki = {}
for znak in zdanie:
    znak=znak.lower()
    if znak not in znaki.keys():
        znaki[znak]=1
    else:
        znaki[znak]+=1
for znak in znaki:
    print(znak,"-",znaki[znak],",", end=" ")
#print(znaki)

#napisać program który:

#- pobierze od uzytkownika wyrażenie; wyrażenie może mieć dowolną liczbę znaków
#(zarówno liter jak i znaków specjalnych)
#- program ma podać długość każdego ze słów w zdaniu
#- program ma podać ile znaków specjalnych jest w zdaniu
#- na koniec program ma podać ile określonych znaków jest w wyrażeniu
#
#Przykładowo wyrażenie:
#
#Ala ma kota, kot ma Alę.
#
#- 3 2 4 3 2 3
#- 2 (licząc spacje 7)
#- a - 6, l - 2, m - 2, k - 2, o - 2, t - 2, ę - 1, , - 1, . - 1