# Exercițiul 12: Eliminarea duplicatelor
# Condiția: Dintr-o listă de orașe cu duplicate, creează un tuplu
# cu orașele unice, păstrând ordinea alfabetică.

orase = ["București", "Cluj", "Iași", "București", "Timișoara", "Cluj", "Constanța", "Iași"]

# # Scrie codul pentru eliminarea duplicatelor și sortare
orase_unice_sortate = tuple(sorted(set(orase)))
print(f"Orasele unice si sortate sunt acestea:",orase_unice_sortate)