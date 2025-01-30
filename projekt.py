import random
arak = [2500, 1500, 1300, "ÜRES"]
ulesek = []
szabadhely = 0
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
jegy = int(input())
if jegy >= 2 and jegy <= 5:
    for ules in ulesek:
        if ules == "ÜRES":
            szabadhely +=1
        else:
            szabadhely = 0 
    if szabadhely >= jegy:
        print("Van egymás mellett megfelelő számú ülőhely.")
    else:
        print("Nincsen az igénynek megfelelő számú ülés egymás mellet.")
else:
    print("2 és 5 közötti mennyiségű jegyet vehet.")
    print("Hány jegyet szeretne venni?")
    jegy = int(input())
    for ules in ulesek:
        if ules == "ÜRES":
            szabadhely +=1
        else:
            szabadhely = 0 
    if szabadhely >= jegy:
        print("Van egymás mellett megfelelő számú ülőhely.")
    else:
        print("Nincsen az igénynek megfelelő számú ülés egymás mellet.")