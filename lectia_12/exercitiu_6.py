"""
Task: Creați o funcție cu numele "task_6" care calculează media unei liste de note.
Parametri: note (obligatoriu - listă), nume_materie (default "Materie necunoscută"), 
          nota_minima_promovare (default 5.0).
Să returneze un dicționar cu: {"materie": nume_materie, "media": media_calculata, 
                               "promovat": True/False, "numar_note": len(note)}
"""
def task_6(note,nume_materie = "Materie necunoscuta", nota_minima_promovare = 5.0):
    if not note:
        media_calculata = 0
    else:
        media_calculata = sum(note) / len(note)
    promovat = media_calculata >= nota_minima_promovare
    return {"materie" : nume_materie,
            "media" : media_calculata,
            "promovat" : promovat,
            "numar_note" : len(note)

    }
print(task_6([5,6,7], "Engleza"))
    