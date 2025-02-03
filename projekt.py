# Felnőtt: 2500 Ft, Diák/nyugdíjas: 2100 Ft, Gyerek: 1300 Ft
import random
arak = ["F", "D/Ny", "Gy", "SZABAD"]
ulesek = []

def nezoter():
    for i in range(15):
        sorok = []
        for ules in range(10):
            sorok.append(random.choice(arak))
        sorok.append("IIII")
        for ules in range(10):
            sorok.append(random.choice(arak))
        ulesek.append(sorok)
        print(sorok)
    return ulesek 
nezoter()

print("Hány jegyet szeretne venni?")

def jegyek():
    szabadhely = 0
    sor = 1
    jegy = int(input())
    if jegy >= 2 and jegy <= 5:
        for i in ulesek:
            for j in i:
                if j == "SZABAD":
                    szabadhely +=1
                else:
                    szabadhely = 0 
                if szabadhely >= jegy:
                    return sor
            sor+=1
    else:
        print("2 és 5 közötti mennyiségű jegyet vehet.")
        print("Hány jegyet szeretne venni?")
        jegy = int(input())
        for i in ulesek:
            for j in i:
                if j == "SZABAD":
                    szabadhely +=1
                else:
                    szabadhely = 0 
                if szabadhely >= jegy:
                    return sor
            sor+=1
print("Ebben a sorban van az igénynek megfelelő számú ülőhely:", jegyek())


