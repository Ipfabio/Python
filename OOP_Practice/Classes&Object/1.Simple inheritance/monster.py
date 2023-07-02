class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')
    
class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Monster.__init__(self, health, energy) dont used anymore
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print('The shark has bitten')

    def move(self):
        print('The shark has move!')
        print(f'The speed of the shark is {self.speed}')

# Exercise
# create scorpion classthat inherits from monster
# health and energy from the parent
# poiston_damage attribute
class Scorpion(Monster):
    def __init__(self, scorpion_health, scorpion_energy, poison_damage):
        super().__init__(health=scorpion_health, energy=scorpion_energy)
        self.poison_damage = poison_damage
    
# overwrite the damage method to show poison damage
    def attack(self):
        print('You are poisoned!')
        print(f'It has dealt {self.poison_damage} poison damage')



# shark = Shark(speed=120, health=100, energy=80)
# print(shark.speed)
# print(shark.health)
# print(shark.energy)

scorpion = Scorpion(100, 80, 50)
print(scorpion.health)
print(scorpion.energy)
print(scorpion.poison_damage)
scorpion.attack()
scorpion.move(5)