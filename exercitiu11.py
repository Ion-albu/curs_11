# Exercițiul 11: Analiza tipurilor de date
# Condiția: Ai un tuplu mixt cu diferite tipuri de date.
# Numără câte elemente sunt numere (int sau float), câte sunt șiruri de caractere,
# și câte sunt de alte tipuri.

date_mixte = (42, "hello", 3.14, True, "world", 100, None, "python", 2.71, False)

# Scrie codul pentru analiza tipurilor
numar_inturi = sum(1 for element in date_mixte if isinstance(element, int))
numar_stringuri = sum(1 for element in date_mixte if isinstance(element, str))
numar_booleane = sum(1 for element in date_mixte if isinstance(element, bool))
print(f"numarul de elemente de tipul int sunt: ",numar_inturi)
print(f"numarul de elemente de tipul string sunt: ",numar_stringuri)
print(f"numarul de elemente de tipul boolean sunt: ",numar_booleane)
