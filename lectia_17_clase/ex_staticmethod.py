class Matematica:
    @staticmethod
    def aduna(a,b):
        return a + b
    
    @staticmethod
    def este_par(numar):
        return numar % 2 == 0
print(Matematica.aduna(1,5))
print(Matematica.este_par(8))
