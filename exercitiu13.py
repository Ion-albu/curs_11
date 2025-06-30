# Exercițiul 13: Procesarea stocului cu while
# Condiția: Ai un dicționar cu produse și cantitățile lor din magazin.
# Folosind un ciclu while, creează un tuplu doar cu numele produselor
# care au stoc mai mare de 5 unități.

stoc_magazin = {
    "lapte": 12,
    "paine": 3,
    "oua": 24,
    "unt": 2,
    "branza": 8,
    "iaurt": 15,
    "miere": 1,
    "cereale": 6
}

# Scrie codul cu while pentru procesarea stocului
produse = list(stoc_magazin.keys())
i = 0
produse_mai_mari_de_5 = []
while i < len(produse):
    produs = produse[i]
    if stoc_magazin[produs] > 5:
        produse_mai_mari_de_5.append(produs)
    i+=1
    rezultat = tuple(produse_mai_mari_de_5)
print(rezultat)
