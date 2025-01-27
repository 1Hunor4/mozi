import random
arak = [2500, 1500, 1300, "ÜRES"]
def nezoter():
    for i in range(15):
        ulesek = []
        for j in range(20):
            ulesek.append(random.choice(arak))
    print(ulesek)
nezoter()