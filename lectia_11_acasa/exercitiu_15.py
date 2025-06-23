"""
Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
"""
def task_15(string):
    string = string.lower()
    return string == string[::-1]


# CODUL TĂU VINE MAI JOS:
# print("Ex 15:")

string = input("Dati un string: ")
print(task_15(string))
# CODUL TĂU VINE MAI SUS: