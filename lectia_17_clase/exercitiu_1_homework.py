nume_prenume = "Ion Albu"
dictionar = {}
suma_ascii = 0

for i in nume_prenume:
    ascii_val = ord(i)
    dictionar[i] = ascii_val
    suma_ascii += ascii_val
print(dictionar)
print(suma_ascii)