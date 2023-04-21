import json

with open('body.json', encoding="utf-8") as hodnoceni:
    data = json.load(hodnoceni)

print(data)

znamky = {}

for jmeno, body in data.items():
    if body >= 60:
        znamky[jmeno] = "Pass"
    else:
        znamky[jmeno] = "Fail"
        
with open("prospech.json", mode = "w", encoding = "utf-8") as file:
    json.dump(znamky, file, ensure_ascii=False)
