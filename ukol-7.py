class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            text = "Potvrzuji zapůjčení vozidla."
            self.dostupne = False
        elif self.dostupne == False:
            text = "Vozidlo není k dispozici."
        return text
        
    
    def get_info(self):
        return f"Vozidlo {self.registracni_znacka}, {self.typ_vozidla}."

    def vrat_auto(self, stav_tach, dny):
        self.najete_km = (self.najete_km + stav_tach)
        self.dny = dny
        self.dostupne = True
        if self.dny < 7:
            self.dny *= 400
        else:
            self.dny *= 300
        return f"Cena za půjčení auta je {self.dny} Kč."
        

    

a1 = Auto("4A2 3020", "Peugeot 403 Cabrio",	47534)
a2 = Auto("1P3 4747", "Škoda Octavia", 41253)
znacka = input("Jakou značku si přejete, Peugeot nebo Škoda? ")
#a1.pujc_auto()
#a2.pujc_auto()
#print(a1.vrat_auto(1000, 8))
#print(a1.najete_km)

if znacka == "Peugeot":
    print(a1.get_info())
    print(a1.pujc_auto())
elif znacka == "Škoda":
    print(a2.get_info())
    print(a2.pujc_auto())