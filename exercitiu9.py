# Exercițiul 9: Verificare condiționată
# Condiția: Verifică dacă numărul 42 există într-un tuplu de numere magice.
# Dacă da, afișează toate pozițiile unde apare.

numere_magice = (7, 13, 42, 23, 42, 99, 42, 17)
numar_cautat = 42

# Scrie codul pentru verificare și găsirea pozițiilor
if numar_cautat in numere_magice:
    indexul = numere_magice.index(numar_cautat)
    print(f"numarul cautat se afla la pozitia :",indexul)
else:
    print("numarul cauttat nu se afla in tupplu",numar_cautat)
