import random
import json

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
            
    def rest(self):
        self.health = 100
        
    def save_to_json(self, file_path="player_data.json"):
        data = {
            "name": self.name,
            "money": self.money,
            "inventory": self.inventory,
            "strength": self.strength,
            "health": self.health,
            "weapon_multiplier": self.weapon_multiplier
        }

        with open(file_path, "w") as file:
            json.dump(data, file)

    def load_from_json(self, file_path="player_data.json"):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.name = data["name"]
                self.money = data["money"]
                self.inventory = data["inventory"]
                self.strength = data["strength"]
                self.health = data["health"]
                self.weapon_multiplier = data["weapon_multiplier"]
        except FileNotFoundError:
            print("No saved data found.")
        
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
        