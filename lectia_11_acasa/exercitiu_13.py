"""
Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 13:")
def task_13(a,b):
    suma = a + b
    produsul = a * b
    return suma, produsul

a = int(input("Dati a: "))
b = int(input("Dati b: "))
print(task_13(a, b))