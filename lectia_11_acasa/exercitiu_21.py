"""
Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 21:")
def task_21(nr):
    cifre = [int(i) for i in str(nr)]
    numar_cifre = len(cifre)
    suma = sum(i ** numar_cifre for i in cifre)
    return suma == nr

nr = int(input("Dati un numar: "))
print(task_21(nr))
# CODUL TĂU VINE MAI SUS: