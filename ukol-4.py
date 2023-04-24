import math

def overeni(cislo):
    if len(nove_cislo) == 9:
        cislo = True
    elif len(nove_cislo) == 13:
        if nove_cislo[0:4] == "+420":
            cislo = True
    else:
        cislo = False
    
    return cislo

cislo = input("Zadej telefonní číslo: ")
nove_cislo = cislo.replace(" ", "")

if overeni(cislo) == True:
    text = input("Zadejte zprávu: ")
else:
    print("Neexistující číslo.")
    exit()

pocet_zprav = math.ceil(len(text) / 180)

def cena(pocet_zprav, KC = 3):
    cena_zpravy = pocet_zprav * KC

    return cena_zpravy

print(f"Cena zprávy je {cena(pocet_zprav, 3)} Kč.")
    