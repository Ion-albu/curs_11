"""
Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 23:")
def task_23(nr):
    if nr <= 0:
        return []
    elif nr == 1:
        return [0]
    fib = [0,1]
    while len(fib) < nr:
        fib.append(fib[-1] + fib[-2])
    return fib


nr = int(input("Dati un numar: "))
print(task_23(nr))
# CODUL TĂU VINE MAI SUS: