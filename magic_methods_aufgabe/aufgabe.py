from math import nan

class Auto:
    def __init__(self, name, ps, emissionen_pro_kg, gewicht):
        self.name = name
        self.ps = ps
        self.emissionen_pro_kg = emissionen_pro_kg
        self.gewicht = gewicht

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        return nan

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        return self - other

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        return self + other

    #Vergleichsoperatoren
    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return NotImplemented


try:
    silvana_caddy = Auto("Caddy", 110, 110, 1500)
    melanie_vw = Auto("Passat", 10, 50, 800)
    number1 = 1
    number2 = 2

    # __add__ Test
    print(silvana_caddy + melanie_vw)
    print(number1 + number2)

    # __sub__ Test
    print(silvana_caddy - melanie_vw)
    print(number1 - number2)
    print(silvana_caddy - number2)

    #Vergleichsoperatoren Test
    print(silvana_caddy * melanie_vw)
    print(silvana_caddy == melanie_vw)
    print(silvana_caddy > melanie_vw)
    print(silvana_caddy < melanie_vw)
except:
    print("An Error occured")