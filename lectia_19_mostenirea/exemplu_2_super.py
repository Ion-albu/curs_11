class Animal:
    def __init__(self, nume, varsta, greutate):
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
    def mananca(self):
        self.greutate += 0.2
class Pisica(Animal):
    def __init__(self, nume, varsta, greutate, culoare_blana):
        super().__init__(nume, varsta,greutate)
        self.culoare_blana = culoare_blana
    def zgaraie(self):
        return "eu zgarai"
    def descriere(self):
        return f"{self.nume} are varsta de {self.varsta} si greutatea de {self.greutate} kg"
    def __str__(self):
        return f"numele:{self.nume}, varsta:{self.varsta}, greutatea {self.greutate}"
obj_pisica = Pisica("tom", 15, 20, "alba")
print(obj_pisica.descriere())
print(obj_pisica)
print(obj_pisica.nume)
print(obj_pisica.culoare_blana)
