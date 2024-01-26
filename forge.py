class Forge:
    
    def __init__(self, player):
        self.player = player
        self.shard_no = 0
        
    def craft_weapon(self, player):
        weapon_choice = input("What weapon would you like to craft?\n1. Iron Sword(4 Iron Shard)\n2. Crystal Sword(4 Crystal Shard)\nYour choice: ")
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
            else:
                print("You don't have enough Crystal Shards!\n")
                
    def craft_armour(self, player):
        armour_choice = input("What armour would you like to craft?\n1. Leather Armour(5 Leather Tunic)\n2. Iron Armour(5 Iron Shard)\nYour choice: ")
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
            else:
                print("You don't have enough Iron Shards!\n")
                
    def equip_item(self, player):
        print("Your inventory:")
        for i, item in enumerate(player.inventory, start=1):
            print(f"{i}. {item}")
        print("\n")
        item_number = int(input("Which item would you like to equip? "))
        print("\n")
        if player.inventory[item_number - 1] == "Iron Sword":
            player.weapon_multiplier = 2
            print("You have equipped an Iron Sword!\n")
        elif player.inventory[item_number - 1] == "Crystal Sword":
            player.weapon_multiplier = 5
            print("You have equipped a Crystal Sword!\n")
        elif player.inventory[item_number - 1] == "Leather Armour":
            player.armour_multiplier = 0.5
            print("You have equipped Leather Armour!\n")
        elif player.inventory[item_number - 1] == "Iron Armour":
            player.armour_multiplier = 0.1
            print("You have equipped Iron Armour!\n")
        else:
            print("You can't equip that!\n")