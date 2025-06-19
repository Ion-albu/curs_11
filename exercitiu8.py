# Exercițiul 8: Căutarea și poziționarea
# Condiția: Într-un tuplu cu note muzicale, găsește poziția notei "Sol".
# Dacă nota nu există, afișează un mesaj corespunzător.

note_muzicale = ("Do", "Re", "Mi", "Fa", "Sol", "La", "Si")
pozitie = note_muzicale.index("Sol")
if "Sol" in note_muzicale:
    print(f"pozitia notei 'Sol' este :",pozitie)
else:
    print("nu este in tuplu")