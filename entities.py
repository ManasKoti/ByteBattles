import random

HIT_CHANCE = [1,1,1,1,1,1,1,1,1,0]

TEMP = 0

class Player:
    
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.inventory = []
        self.strength = 100
        self.health = 100
        self.weapon_multiplier = 1
        
    def attack(self, enemy):
        if random.choice(HIT_CHANCE) == 1:
            enemy.health -= self.strength * random.uniform(0.05, 0.1) * self.weapon_multiplier
            print("You hit the enemy!")
        else:
            print("You missed!")
        
class Wolf:
        
    def __init__(self):
        self.name = "Wolf"
        self.strength = 50
        self.health = 50

    def attack(self, player):
        if random.choice(HIT_CHANCE) == 1:
            player.health -= self.strength * random.uniform(0.05, 0.1)
            print("The enemy hit you!")
        else:
            print("The enemy missed!")
            
class Bandit:
    
    def __init__(self):
        self.name = "Bandit"
        self.strength = 100
        self.health = 100
        
    def attack(self, player):
        if random.choice(HIT_CHANCE) == 1:
            player.health -= self.strength * random.uniform(0.05, 0.1)
            print("The enemy hit you!")
        else:
            print("The enemy missed!")
        
class Troll:
    
    def __init__(self):
        self.name = "Troll"
        self.strength = 200
        self.health = 200
        
    def attack(self, player):
        if random.choice(HIT_CHANCE) == 1:
            player.health -= self.strength * random.uniform(0.05, 0.1)
            print("The enemy hit you!")
        else:
            print("The enemy missed!")
        