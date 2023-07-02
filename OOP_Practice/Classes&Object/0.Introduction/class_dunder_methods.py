from typing import Any


class Monster:

    def __init__(self, health, energy): # Metodo constructor
        self.health = health
        self.energy = energy

    def __len__(self): 
        return self.health
    
    def __abs__(self): # Convierte en valores absolutos (negativo a positivo)
        return self.energy
    
    def __call__(self): # Aparece al ser invocado
        print('The monster was called')

    def __add__(self, other): # Añade a lo que tenemos
        return self.health + other
    
    def __str__(self): # Nos permite personalizar información que se presenta al llamar al objeto
        return f'A monster with health {self.health} and energy {self.energy}'

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        monster.energy -= 20
        print(self.energy)

    def move(self, speed):
        print('The monster has move')
        print(f'It has a speed of {speed}')

monster = Monster(10, 20)
print(str(monster))
print(monster)