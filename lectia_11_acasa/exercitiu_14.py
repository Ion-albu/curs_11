"""
Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane și returnează textul "minor" dacă vârsta este sub 18 ani, "adult" dacă vârsta este între 18 și 65 ani și "senior" dacă vârsta este peste 65 de ani.
Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 14:")
def task_14(varsta):
    if varsta < 18:
        return "minor"
    elif 18 <= varsta <= 65:
        return "adult"
    else:
        return "senior"

varsta = int(input("Dati varsta: "))
print(task_14(varsta))
# CODUL TĂU VINE MAI SUS: