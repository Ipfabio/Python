# scope problem
def update_health(amount):
    monster.health += amount

# health = 10
# print(health)
# update_health(20)
# print(health)

class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
        # self.energy = self.set_energy(energy)
        # self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount
    
    # def set_energy(self,energy):
    #     new_energy = energy * 2
    #     # return new_energy
    #     self.energy = new_energy

# (2). The monster class should have a method that lowers the health -> get_damage(amount)
    def get_damage(self,amount):
        self.health -= amount

# Exercise
# (1). Create a Hero class with 2 parameters: damage, monster
class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

# (3). The Hero class should have an attack method that calls the get_damage method from monster the amount of damage is hero.damage()
    def attack(self):
        self.monster.get_damage(self.damage)

monster = Monster(health=100, energy=50)

hero = Hero(damage=15, monster=monster)
print(monster.health)
hero.attack()
print(monster.health)