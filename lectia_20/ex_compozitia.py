class Motor:
    def __init__(self, putere):
        self.putere = putere
    
class Masina:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor

    def porneste(self):
        return f"masina porneste motorul cu puterea {self.motor.putere}"
    def afiseaza(self):
        return print(self.porneste())
motor = Motor(200)
masina = Masina("ford", motor)
print(masina.porneste())
