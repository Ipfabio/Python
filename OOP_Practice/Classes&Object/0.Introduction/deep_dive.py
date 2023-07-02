# def add(a,b):
#     return a + b

# class Test:
#     def __init__(self, add_function):
#         self.add_functions = add_function

# test = Test(add_function= add)
# print(test.add_functions(1,2))

# Create a Monster class with a parameter called func, store this func as parameter
class Monster:
    def __init__(self,func):
        self.func = func

# Create anohter class, called Attacks, that has 4 methods:
# bite, strike, slash, kick (each method just prints some text)
class Attack:
    def bite(self):
        print('has Bite')

    def strike(self):
        print('has Strike')

    def slash(self):
        print('has Slash')

    def kick(self):
        print('has Kick')
#  Create a monster object and give it one of the attack method from the attacks class
attacks = Attack()
monster = Monster(func=attacks.bite())
monster.func()
