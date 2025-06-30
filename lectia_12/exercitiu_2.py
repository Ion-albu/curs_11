"""
Task: Creați o funcție cu numele "task_2" care calculează pretul total pentru o comandă.
Funcția primește: pretul_unitar (obligatoriu), cantitate (default 1), reducere_procent (default 0).
Să returneze: pret_unitar * cantitate * (1 - reducere_procent/100)
Exemplu: task_2(100) -> 100.0
         task_2(100, 3) -> 300.0  
         task_2(100, 2, 10) -> 180.0
"""
def task_2(pret_unitar,cantitate = 1,reducere_procent = 0):
    return pret_unitar * cantitate * (1 - reducere_procent/100)
print(task_2(100))