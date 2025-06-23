
"""
Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
"""
def task_4(matrice):
    lista_aplatizata = []
    for sublist in matrice:
        for x in sublist:
            lista_aplatizata.append(x)
    return lista_aplatizata
rezultat = task_4([[1, 2], [3, 4], [5, 6]])
print(rezultat)
