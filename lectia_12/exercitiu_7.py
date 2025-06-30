
"""
Task: Creați o funcție cu numele "task_7" care generează un mesaj de întâmpinare pentru un website.
Parametri: nume_utilizator (obligatoriu), tip_cont (default "standard"), 
          prima_vizita (default False), limba (default "ro").
Mesajele să fie:
- română + prima vizită: "Bun venit pentru prima dată, [nume] ([tip_cont])!"
- română + vizită repetată: "Bine ai revenit, [nume] ([tip_cont])!"  
- engleză + prima vizită: "Welcome for the first time, [nume] ([tip_cont])!"
- engleză + vizită repetată: "Welcome back, [nume] ([tip_cont])!"
"""
def task_7(nume_utilizator, tip_cont = "standart", prima_vizita = False, limba = "ro"):
    if limba == "ro":
        if prima_vizita:
            mesaj = f"Bun venit pentru prima data,{nume_utilizator} ({tip_cont})!"
        else:
            mesaj = f"Bine ai revenit, {nume_utilizator} ({tip_cont})!"
    elif limba =="engleza":
        if prima_vizita:
            mesaj = f"Welcome for the first time,{nume_utilizator} ({tip_cont})!"
        else:
            mesaj = f"Welcome back, {nume_utilizator} ({tip_cont})!"
    else:
        mesaj = f"Limba necunoscuta pentru utilizatorul {nume_utilizator} ({tip_cont})!"
    return mesaj
print(task_7("ion", prima_vizita= False))
print(task_7("Maria", prima_vizita= True))
print(task_7("ion", prima_vizita= False, limba= "engleza"))
print(task_7("Johny", prima_vizita= True, limba= "engleza"))
print(task_7("ion",limba="CHINEZA"))