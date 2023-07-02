class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
    
    def attack(self):
        self.monster.get_damage(self.damage)