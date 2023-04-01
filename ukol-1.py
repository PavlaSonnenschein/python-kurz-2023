jmeno = ("Pavla")

print(f"{jmeno}@czechitas.cz")

jmeno_a_prijmeni = input("Jméno a příjmení: ")

print(jmeno_a_prijmeni .upper())
print(jmeno_a_prijmeni .lower())

print(jmeno_a_prijmeni[0].upper() + jmeno_a_prijmeni[1:5+1] + jmeno_a_prijmeni[6].upper() + jmeno_a_prijmeni[7:])

print(jmeno_a_prijmeni[0].upper() + ". " + jmeno_a_prijmeni[6].upper() + ".")

rozdeleni = jmeno_a_prijmeni.split()
if len(rozdeleni[0]) > 5:
    print(rozdeleni[0][0].upper() + rozdeleni[1][0].upper() + rozdeleni[1][1:])
else:
    print(jmeno_a_prijmeni)

print(jmeno_a_prijmeni[0:1] + jmeno_a_prijmeni[1].upper() + jmeno_a_prijmeni[2:8] + jmeno_a_prijmeni[8:10].upper() + jmeno_a_prijmeni[10:])