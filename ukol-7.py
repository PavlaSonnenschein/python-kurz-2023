class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        self.dostupne = False
    
    def __str__(self):
        if self.dostupne:
            text = "Potvrzuji zapůjčení vozidla."
        else:
            text = "Vozidlo není k dispozici."
        return text
    
    def get_info(self):
        return f"Vozidlo {self.registracni_znacka}, {self.typ_vozidla}."
    

A1 = Auto("4A2 3020", "Peugeot 403 Cabrio",	"47534")
A2 = Auto("1P3 4747", "Škoda Octavia", "41253")
znacka = input("Jakou značku si přejete, Peugeot nebo Škoda? ")
#A1.pujc_auto()
#A2.pujc_auto()

if znacka == "Peugeot":
    print(A1.get_info())
    print(A1)
else :
    print(A2.get_info())
    print(A2)