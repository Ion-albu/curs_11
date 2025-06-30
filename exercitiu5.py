 #Exercițiul 5: Navigarea în tuplu
# Condiția: Creează un tuplu cu zilele săptămânii.
# Accesează prima zi, ultima zi și ziua din mijlocul săptămânii.

# Scrie codul aici
zilele_saptamanii = ("luni","marti","miercuri","joi","vineri","sambata","duminica")
for i in zilele_saptamanii:
    prima_zi = zilele_saptamanii[0]
    ultima_zi = zilele_saptamanii[-1]
    ziua_mijloc = zilele_saptamanii[3]

print(f"prima zi din saptamana este: {prima_zi} \nultima zi din saptamana este: {ultima_zi}")
print(f"ziua din mijloc a saptamanii este: {ziua_mijloc}")
