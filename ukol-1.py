jmeno = ("Pavla")

print(f"{jmeno}@czechitas.cz")

jmeno_a_prijmeni = input("Jméno a příjmení: ")
rozdeleni = jmeno_a_prijmeni.split()

print(jmeno_a_prijmeni .upper())
print(jmeno_a_prijmeni .lower())

print(rozdeleni[0][0].upper() + rozdeleni[0][1:].lower() + " " + rozdeleni[1][0].upper() + rozdeleni[1][1:].lower())

print(rozdeleni[0][0].upper() + ". " + rozdeleni[1][0].upper() + ".")

if len(rozdeleni[0]) > 5:
    print(rozdeleni[0][0].upper() + " "+ rozdeleni[1][0].upper() + rozdeleni[1][1:].lower())
else:
    print(rozdeleni[0][0].upper() + rozdeleni[0][1:].lower() + " " + rozdeleni[1][0].upper() + rozdeleni[1][1:].lower())

print(jmeno_a_prijmeni[0:1] + jmeno_a_prijmeni[1].upper() + jmeno_a_prijmeni[2:8] + jmeno_a_prijmeni[8:10].upper() + jmeno_a_prijmeni[10:])