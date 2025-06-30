# Exercițiul 1: Inversarea cheilor și valorilor în dicționar
# Condiția: Ai un dicționar cu informații despre studenți și notele lor.
# Creează un dicționar inversat unde notele sunt chei și numele sunt valori.
# Afișează ambele dicționare.

studenti_note = {
    "Ana": 9,
    "Bogdan": 8,
    "Carmen": 10,
    "Dan": 7,
    "Elena": 9,
    "Florin": 6,
    "Gabriela": 8,
    "Horia": 10
}

# Scrie codul aici pentru inversare
inversat = {}
for cheie,valoare in studenti_note.items():
    if valoare in inversat:
        inversat[valoare].append(cheie)
    else:
        inversat[valoare]=[cheie]
print(inversat)