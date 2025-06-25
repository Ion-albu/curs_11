"""
Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 19:")
def task_19(nr):
    if nr < 2:
        return False
    for i in range(2, int(nr**0.5)+1):
        if nr % i == 0:
            return False
    return True

num = int(input("Dati un numar: "))
print(task_19(num))
# CODUL TĂU VINE MAI SUS: