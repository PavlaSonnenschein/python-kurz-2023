teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumer = [round((sum(teplota))/4, 3) for teplota in teploty]
print(prumer)

ranni_teploty = [teplota[0] for teplota in teploty]
print(ranni_teploty)

nocni_teploty = [teplota[3] for teplota in teploty]
print(nocni_teploty)

poledne_noc = [
        [teplota [1]] + [teplota[3]]
        for teplota in teploty
]

print(poledne_noc)