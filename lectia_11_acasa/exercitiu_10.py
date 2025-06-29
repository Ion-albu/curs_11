"""
Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 10:")
def task_10(nume, varsta,oras = "Necunoscut"):
    return f"Nume: {nume}, varsta: {varsta}, Orasul:{oras}"


nume = input("Dati un nume: ")
varsta = int(input("Dati varsta: "))
oras = input("Dati orasul (optional): ")
print(task_10(nume, varsta, oras))
# CODUL TĂU VINE MAI SUS: