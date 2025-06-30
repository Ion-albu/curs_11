"""
Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 20:")
def task_20(nr):
    if nr < 2:
        return False
    
    suma_divizorilor = 0
    for i in range(1, nr):
        if nr % i == 0:
            suma_divizorilor += 1

    return suma_divizorilor == nr


nr = int(input("Dati un numar: "))
print(task_20(nr))
# CODUL TĂU VINE MAI SUS: