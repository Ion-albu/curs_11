
"""
Task: Creați o funcție cu numele "task_1" care primește numele unei persoane ca parametru obligatoriu 
și vârsta ca parametru opțional (default 18). Funcția să returneze un string în formatul: 
"Numele: [nume], Vârsta: [vârsta] ani"
Exemplu: task_1("Ana") -> "Numele: Ana, Vârsta: 18 ani"
         task_1("Ion", 25) -> "Numele: Ion, Vârsta: 25 ani"
"""
def task_1(nume, varsta = 18):
    return f"numele: {nume}, Varsta: {varsta}"
print(task_1("Ion",29))