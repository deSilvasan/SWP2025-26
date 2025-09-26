import random

ausgabeArr = []
sechsZuege = []
statistikDict = {}

def zufallszahlenGenerieren(obergrenze):
    for i in range(obergrenze):
        wert = i+1
        ausgabeArr.append(wert)

def zufallszahlenGenerator(obergrenze, zuege):
    arrayGrenze = obergrenze-1
    #random.shuffle(ausgabeArr)
    #Schleife für Zufallsgenerator
    for i in range(zuege):
        # Zufallszahl wird generiert
        zufallszahl = random.randrange(arrayGrenze + 1)
        # Zufallszahl wird im Array verschoben
        sechsZuege.append(ausgabeArr[zufallszahl])
        letzteStelleArray = ausgabeArr[arrayGrenze]
        ausgabeArr[arrayGrenze] = ausgabeArr[zufallszahl]
        ausgabeArr[zufallszahl] = letzteStelleArray
        arrayGrenze = arrayGrenze - 1

def häufigkeitenZufallszahlen(array):
    for element in array:
        statistikDict[element] = statistikDict.get(element, 0) + 1

def relativeHäufigkeitZufallszahlen(gesamtziehungen):
    for element in statistikDict:
        statistikDict[element] = statistikDict.get(element) / gesamtziehungen

for e in range(1000):
    sechsZuege = []
    ausgabeArr = []
    zufallszahlenGenerieren(45)
    zufallszahlenGenerator(45,6)
    häufigkeitenZufallszahlen(sechsZuege)

print("Wie oft die Zahlen gezuben wurden:")
print(statistikDict)
relativeHäufigkeitZufallszahlen(1000)
sortiertes_dict = dict(sorted(statistikDict.items()))
print(" ")
print("Die sortierten Häufigkeiten davon: ")
print(sortiertes_dict)

