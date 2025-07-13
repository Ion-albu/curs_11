class Motor:
    def __init__(self, tip):
        self.tip = tip
class Masina:
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor("electric")
    def __str__(self):
        return f"marca {self.marca}, cu motorul {self.motor.tip}"

masina = Masina("bmw")
print(masina)

        