"""
Task: Creați o funcție cu numele "task_4" care calculează aria unei forme geometrice.
Parametri: forma (obligatoriu - "dreptunghi", "triunghi", "cerc"), a (obligatoriu), b (default None).
- Pentru dreptunghi: aria = a * b (b este obligatoriu)
- Pentru pătrat (când forma="dreptunghi" și b=None): aria = a * a  
- Pentru triunghi: aria = a * b / 2 (b este obligatoriu)
- Pentru cerc: aria = 3.14159 * a * a (a este raza, b se ignoră)
Returnează aria calculată sau -1 dacă parametrii sunt invalizi.
"""
def task_4(forma, a, b=None):
    if forma == "dreptunghi":
        if b is not None:
            aria = a * b
            return f"aria dreptunghiului este: {aria}"
        else:
            return f"aria patratului este: {a * a}"
    elif forma == "triunghi":
        if b is not None:
            return f"aria triunghiului este : {a * b / 2}"
        else:
            return -1
    elif forma == "cerc":
        return f"aria cercului este : {3.14159 * a * a}"
    else:
        return -1
    
print(task_4("dreptunghi", 2,3))
print(task_4("dreptunghi", 2,))
print(task_4("triunghi", 2,3))
print(task_4("triunghi",3))
print(task_4("cerc", 2))
print(task_4("cerc", 2))
