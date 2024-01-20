from entities import *
from battle import battle
import random

#List of random encounters
#1.Nothing 2.Wolf 3.Bandit 4.Troll 5.Loot
random_wild_encounter = [1,1,1,2,2,2,3,3,4,5]

#Inventory
money = 0
Inventory = []

#Game loop
game_on = True
while game_on:
    
    player_name = input("Welcome to Byte Battles!!\nWhat is your name adventurer your name?\n")
    print("Welcome " + player_name + "!\n")
    player = Player(player_name)
    
    player_alive = True
    while player_alive:
    
        turn_action = input("What would you like to do?\n1. Explore\n2. Visit Shop\n3. Visit Inn\nYour choice: ")
        print()
                
        #Explore
        if turn_action == "1":
            encounter = random.choice(random_wild_encounter)
            #No encounter
            if encounter == 1:
                result = None
                print("You didn't encounter anything.")
            #Wolf encounter
            elif encounter == 2:
                wolf = Wolf()
                result = battle(player, wolf)
            #Bandit encounter
            elif encounter == 3:
                bandit = Bandit()
                result = battle(player, bandit)
            #Troll encounter
            elif encounter == 4:
                troll = Troll()
                result = battle(player, troll)
            #Loot found
            elif encounter == 5:
                result = None
                loot_found = random.choice([0,1,2])
                #Money found
                if loot_found == 0:
                    money_found = random.choice([10,20,30,40,50])
                    print(f"You found {money_found} gold!")
                    money += money_found
                #Item found
                elif loot_found == 1:
                    item_found = random.choice(["Leather Tunic", "Iron Shard", "Crystal Shard"])
                    print(f"You found a {item_found}!")
                    Inventory.append(item_found)
                #Boss item found
                elif loot_found == 2:
                    print("You foung a Dragon Scale!")
                    Inventory.append("Dragon Scale")
            #Check if player is dead
            if result == "dead":
                player_alive = False
                replay = input("Would you like to play again? (y/n) ")
                if replay == "n":
                    game_on = False
                    break