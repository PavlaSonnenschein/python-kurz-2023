sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Kód součástky: ")


if kod in sklad:
    hodnota = int(input("Množství: "))
    if hodnota == sklad[kod]:
        print ("Objednávku připravíme.")
        sklad.pop(kod)
    elif hodnota < sklad[kod]:
        print("Objednávku připravíme.")
        sklad[kod] += -hodnota
    elif hodnota > sklad[kod]:
        print(f"Je možné prodat pouze {sklad[kod]} kusů.")
        sklad.pop(kod)
else:
    print("Součástka není skladem.")

print(sklad)