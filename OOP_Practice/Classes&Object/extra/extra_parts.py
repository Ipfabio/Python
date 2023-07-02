class Monster:
    '''A monster that has some attribute'''

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # private attributes (work for attributes and methods)
        self._id = 5

    # methods
    def attack(self, amount):
        print('The monsterhas attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20
    
    def move(self, speed):
        print('The mosnter has moved')
        print(f'It has a speed of {speed}')

monster = Monster(20, 10)


# hasattr and setattr (allows us to check if a class has an attribute and we can also use it to set an attribute)
# hasattr(object, 'attribute') -> return boolean

# if hasattr(monster, 'health'):
#     print(f'The monster has {monster.health} health')

# setattr(object, 'attribute', value)
setattr(monster, 'weapon', 'Sword')
# similar to -> monster.weapon = 'Sword' 
# print(monster.weapon)

# new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion', 'mana'])
# for attr, value in new_attributes:
#     setattr(monster,attr,value)
# print(vars(monster))

# doc
# print(monster.__doc__)

# help([])