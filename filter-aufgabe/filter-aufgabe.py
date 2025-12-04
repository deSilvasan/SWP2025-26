names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

def bedingung(tuple):
    if((tuple[1]>= 18) and (tuple[2]>=80)):
        return True
    return False

ergebnis = list(filter(bedingung,list(zip(names,ages,scores))))

endergebnis = list(map(lambda x: {"name":x[0], "age":x[1], "score":x[2]}, ergebnis))
print(endergebnis)