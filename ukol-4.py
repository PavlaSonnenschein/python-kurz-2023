import math

def overeni(cislo):
    if len(cislo) == 9:
        cislo = True
    elif len(cislo) == 13:
        if cislo[0:4] == "+420":
            cislo = True
    else:
        cislo = False
    
    return cislo

cislo = input("Zadej telefonní číslo: ")

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
    