class Forge:
    
    def __init__(self, player):
        self.player = player
        self.shard_no = 0
        
    def craft_weapon(self, player):
        weapon_choice = input("What weapon would you like to craft?\n1. Iron Sword\n2. Crystal Sword\nYour choice: ")
        if weapon_choice == "1":
            for item in self.player.inventory:
                if item == "Iron Shard":
                    self.shard_no += 1
            if self.shard_no >= 4:
                print("You have crafted an Iron Sword!\n")
                self.player.inventory.append("Iron Sword")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.shard_no = 0
                player.weapon_multiplier = 2
            else:
                print("You don't have enough Iron Shards!\n")
        elif weapon_choice == "2":
            for item in self.player.inventory:
                if item == "Crystal Shard":
                    self.shard_no += 1
            if self.shard_no >= 4:
                print("You have crafted a Crystal Sword!\n")
                self.player.inventory.append("Crystal Sword")
                self.player.inventory.remove("Crystal Shard")
                self.player.inventory.remove("Crystal Shard")
                self.player.inventory.remove("Crystal Shard")
                self.player.inventory.remove("Crystal Shard")
                self.shard_no = 0
                player.weapon_multiplier = 5
            else:
                print("You don't have enough Crystal Shards!\n")
                
    def craft_armour(self, player):
        armour_choice = input("What armour would you like to craft?\n1. Leather Armour\n2. Iron Armour\nYour choice: ")
        if armour_choice == "1":
            for item in self.player.inventory:
                if item == "Leather Tunic":
                    self.shard_no += 1
            if self.shard_no >= 5:
                print("You have crafted Leather Armour!\n")
                self.player.inventory.append("Leather Armour")
                self.player.inventory.remove("Leather Tunic")
                self.player.inventory.remove("Leather Tunic")
                self.player.inventory.remove("Leather Tunic")
                self.player.inventory.remove("Leather Tunic")
                self.player.inventory.remove("Leather Tunic")
                self.shard_no = 0
                player.armour_multiplier = 0.5
            else:
                print("You don't have enough Leather Tunics!\n")
        elif armour_choice == "2":
            for item in self.player.inventory:
                if item == "Iron Shard":
                    self.shard_no += 1
            if self.shard_no >= 5:
                print("You have crafted Iron Armour!\n")
                self.player.inventory.append("Iron Armour")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.player.inventory.remove("Iron Shard")
                self.shard_no = 0
                player.armour_multiplier = 0.1
            else:
                print("You don't have enough Iron Shards!\n")