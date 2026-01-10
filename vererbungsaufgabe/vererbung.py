from abc import abstractmethod


class Fahrzeug:
    antrieb = "KA"
    def __init__(self, name: str, fahrgestellnummer: int, unfaelle: int, baujahr: int):
        self.name = name
        self.fahrgestellnummer = fahrgestellnummer
        self.unfaelle = unfaelle
        self.baujahr = baujahr

    def fahrzeugalter(self, aktuellesJahr: int):
        return f"Das Fahrzeug ist schon {aktuellesJahr-self.baujahr} alt."

    @abstractmethod
    def antrieb_ausgeben(self):
        pass

    def __str__(self):
        return (f"Ein Fahrzeug namens {self.name} mit der Fahrgestellnummer {self.fahrgestellnummer}. Wurde im Jahr "
                f"{self.baujahr} gebaut und hatte bis jetzt {self.unfaelle} Unfälle.")

class Elektroauto(Fahrzeug):
    def __init__(self, name, fahrgestellnummer, unfaelle, baujahr):
        super().__init__(name, fahrgestellnummer, unfaelle, baujahr)
        self.antrieb = "Elektro"

    def unfaelle_ausgeben(self):
        return f"Das Elektroauto hatte schon {self.unfaelle} Unfälle."

    def antrieb_ausgeben(self):
        return f"Das Elektroauto hat einen {self.antrieb} Antrieb."

class Benzinerauto(Fahrzeug):
    def __init__(self, name, fahrgestellnummer, unfaelle, baujahr):
        super().__init__(name, fahrgestellnummer, unfaelle, baujahr)
        self.antrieb = "Benziner"

    def antrieb_ausgeben(self):
        return f"Der Benziner hat einen {self.antrieb} Antrieb."

# Instanzen erzeugen
e_auto = Elektroauto("Tesla Model 3", 123456, 1, 2020)
b_auto = Benzinerauto("VW Golf", 654321, 3, 2015)

# Methoden aufrufen
print(e_auto.fahrzeugalter(2026))
print(b_auto.fahrzeugalter(2026))

print(e_auto.antrieb_ausgeben())
print(b_auto.antrieb_ausgeben())

# __str__ Aufrufe
print(e_auto)
print(b_auto)

# Polymorphie (Basisklassen-Referenz)
fahrzeuge = [e_auto, b_auto]

for f in fahrzeuge:
    print(f.antrieb_ausgeben())
    print(f.fahrzeugalter(2026))

# Attribute ändern
e_auto.unfaelle += 1
b_auto.unfaelle = 0

# Erneuter Methodenaufruf nach Änderung
print(e_auto.unfaelle_ausgeben())
print(b_auto.antrieb_ausgeben())