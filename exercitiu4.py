# Exercițiul 4: Extinderea unui tuplu
# Condiția: Ai un tuplu cu coordonatele (x, y) ale unui punct.
# Adaugă coordonata z pentru a crea un punct 3D prin concatenare.

punct_2d = (3, 7)
z_coord = 12
#1 metoda
modifca = set(punct_2d)
modifca.add(8)
print(modifca)

# # a 2 metoda prin concatenare
punct_3d = punct_2d + (2,)
print(punct_3d)