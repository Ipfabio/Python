from hero import Hero
from monster import Monster

monster1 = Monster(100, 50)
hero = Hero(15,monster1)

print(monster1.health)
hero.attack()
print(monster1.health)
