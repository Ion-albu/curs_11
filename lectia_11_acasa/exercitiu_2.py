"""
Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
Utilizați list comprehension în proces
"""

def task_2():
    return [x **2 for x in range(1,11)]
print(f"afisam exemplul cu list comprehension {task_2()}")

"""
Exemplu cu for
"""
def task_2_1():
    lista = []
    for x in range(1,11):
         lista.append(x**2)
  
    return lista
print(f"afisam exemplul cu for:", task_2_1())