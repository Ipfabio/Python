class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def get_damage(self, amount):
        self.health -= amount