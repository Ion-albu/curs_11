class pokemon:
    def __init__(self, name, pokemon_type, health):
        self.name = name
        self.pokemon = pokemon_type
        self.health = health
    
    def attack(self):
        print(f"{self.name} Ataca!")

    def dodge(self):
        print(f"{self.name} se fereste") 

    def evolve(self):
        print(f"{self.name} evolueaza")
pikachu = pokemon("pikachu" , "electric", 80)
pikachu.attack()
pikachu.dodge()
print(pikachu.health)
print(pikachu.pokemon)
print(pikachu.name)
pikachu.evolve()