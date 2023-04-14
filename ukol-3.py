import json

with open('body.json', encoding="utf-8") as hodnoceni:
    data = json.load(hodnoceni)

print(data)

body = {
    "Dušan Kadlec": 32,
    "Daniel Svoboda": 100,
    "Anežka Benešová": 17,
    "Andrea Vaňková": 15,
    "Robin Blažek": 100,
    "Renáta Tichá": 81,
    "Matyáš Vaněk": 23,
    "Tereza Procházková": 3,
    "Luboš Černý": 64,
    "Vasyl Novotný": 66,
    "Jaroslav Polák": 7,
    "Dušan Kříž": 63,
    "Vlasta Kadlecová": 20,
    "Zdenka Soukupová": 100,
    "Stanislav Vaněk": 90,
    "Julie Poláková": 40,
    "Veronika Fialová": 53,
    "Květoslava Dvořáková": 52,
    "Ladislav Čermák": 76,
    "Dana Marková": 98,
    "Miloš Horák": 78,
    "Štefan Jelínek": 37,
    "Miloš Veselý": 25,
    "Aleš Kříž": 22,
    "Marcela Machová": 11,
    "Blanka Kučerová": 67,
    "Šárka Marešová": 81,
    "Dalibor Kadlec": 8,
    "Robert Pospíšil": 36
}

for jmeno in body:
    if body[jmeno] >= 60:
        body[jmeno] = ("Pass")
    else:
        body[jmeno] = ("Fail")

with open("prospech.json", mode = "w", encoding = "utf-8") as file:
    ensure_ascii=False
    json.dump(body, file, ensure_ascii=False)
