import json

with open('body.json', encoding="utf-8") as hodnoceni:
    data = json.load(hodnoceni)

print(data)

for jmeno in data:
    if data[jmeno] >= 60:
        data[jmeno] = ("Pass")
    else:
        data[jmeno] = ("Fail")

with open("prospech.json", mode = "w", encoding = "utf-8") as file:
    json.dump(data, file, ensure_ascii=False)
