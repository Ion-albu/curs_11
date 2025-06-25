"""
Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 22:")
def task_22(nr):
    suma_cifre = sum(int(i) for i in str(nr))
    return nr % suma_cifre == 0


nr = int(input("Dati un numar: "))
print(task_22(nr))
# CODUL TĂU VINE MAI SUS:
