"""
Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
"""
def task_24(nr):
    if nr <= 0:
        return []
    return [i for i in range(1, nr +1) if nr % i == 0]
nr = int(input("introducem un nr:"))
print(task_24(nr))
