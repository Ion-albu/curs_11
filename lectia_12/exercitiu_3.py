"""
Task: Creați o funcție cu numele "task_3" care afișează informații despre un film.
Parametri: titlu (obligatoriu), an (default 2024), gen (default "Dramă"), durata_minute (default 120).
Funcția să afișeze: "Film: [titlu], An: [an], Gen: [gen], Durata: [durata] minute"
"""
def task_3(titlu, an = 2024, gen = "drama", durata_minute = 120):
    return f"Film: {titlu}, an: {an} gen: {gen},durata: {durata_minute}"
print(task_3("Major"))
