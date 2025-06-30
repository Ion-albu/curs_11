"""
Task: Creați o funcție cu numele "task_5" care creează un profil de utilizator.
Parametri: nume (obligatoriu), email (obligatoriu), varsta (default 18), 
          oras (default "Necunoscut"), activ (default True).
Să returneze un dicționar cu toate informațiile.
Exemplu: task_5("Ana", "ana@email.com") -> 
         {"nume": "Ana", "email": "ana@email.com", "varsta": 18, "oras": "Necunoscut", "activ": True}
"""
def task_5(nume, email,varsta=18, oras = "Necunoscut", activ = True):
    return {"nume": nume, "email": email, "vasrsta": varsta, "oras": oras, "activ": activ}
print(task_5("Ana", "ana@mail.com",20,"Chisinau",False))