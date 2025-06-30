"""
Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
Utilizați list comprehension în proces.
"""
def task_3():
    return [x for x in range(1,11) if x % 2 != 0]
print(task_3())