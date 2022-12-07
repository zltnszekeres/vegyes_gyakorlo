"""
szemelyek = ["Ákos", "Béla", "Éva", "Zoli", "Judit"]

nemek = ["férfi", "férfi", "nő", "férfi", "nő"]
i = len(nemek)-1
utolsoferfi = ""

while i >= 0 and nemek[i] == "nő":
    i -= 1

if i >= 0:

    print (szemelyek[i])
else:
    print("nincs ferfi")
j = 0
utolso_ferfi = ""

while(j < len(nemek)):
    if nemek[j] == "ferfi":
        utolso_ferfi = szemelyek[j]
print(szemelyek[j])

i = -1
while nemek[i] != "férfi":
    i -=1

print(szemelyek[i])
"""
import random
sorozat = [-3, 5, 11, -2, 4]

def kiir (sep = " "):
    szamsor = ""
    i = 0
    while i < len(sorozat)-1:

        szamsor += str(sorozat[i]) + sep
        i += 1
    print(f'A tömb elemeinek kiírása {szamsor}{i}')

kiir("@")

print("első feladat")
veletlen_szam = random.randint(5,12)
sorozat[0] += veletlen_szam
print('A tömb első elemének megnövelése egy véletlen számmal, az [5,12] intervallumon belül: ')
print(sorozat)
print('2. feladat')

def bekeres ():

    ujra = True
    while ujra:
        utolso_elem = int(input('Add meg a tömb utolsó elemét : '))

        if utolso_elem %2 != 0  and utolso_elem %3 == 0 and utolso_elem < 100 and utolso_elem > 9:
            ujra = False
            print(f'Jó számot adtál meg, az utolsó elem: {utolso_elem}')
bekeres()

print('3. feladat')
kiir()

print('4. feladat')

def ketjegyu ():
    i = 0

    while i < len(sorozat) and (sorozat[i] < 10 or sorozat[i] > 100):

        i += 1


    print(f'A  kétjegyű szám {sorozat[i]} a {i+1} elem')
ketjegyu()












