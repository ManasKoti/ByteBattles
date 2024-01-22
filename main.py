from entities import *
from battle import battle
from shop import Shop
from forge import Forge
import random

#List of random encounters
#1.Nothing 2.Wolf 3.Bandit 4.Troll 5.Loot 6.Dragon Scale
random_wild_encounter = [1,1,1,2,2,2,3,3,4,5,6]
shard_no = 0

#Game loop
game_on = True
while game_on:
     
    player_name = input("Welcome to Byte Battles!!\nWhat is your name adventurer your name?\n")
    print()
    print("Welcome " + player_name + "!\n")
    player = Player(player_name)
    
    player_alive = True
    while player_alive:
    
        turn_action = input("What would you like to do?\n1. Explore\n2. Visit Shop\n3. Visit Inn\n4. Visit Forge\n5. Summon Dragon\n6. Save Game\n7. Load Game\nYour choice: ")
        print()
                
        #Explore
        if turn_action == "1":
            encounter = random.choice(random_wild_encounter)
            #No encounter
            if encounter == 1:
                result = None
                print("You didn't encounter anything.\n")
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
                loot_found = random.choice([0,1])
                #Money found
                if loot_found == 0:
                    money_found = random.choice([10,20,30,40,50])
                    print(f"You found {money_found} gold!\n")
                    player.money += money_found
                #Item found
                elif loot_found == 1:
                    item_found = random.choice(["Leather Tunic", "Iron Shard", "Crystal Shard"])
                    print(f"You found a {item_found}!\n")
                    player.inventory.append(item_found)
            #Dragon Scale found
            elif encounter == 6:
                result = None
                print("You found a Dragon Scale!\n")
                player.inventory.append("Dragon Scale")
            
            #Check if player is dead
            if result == "dead":
                player_alive = False
                replay = input("Would you like to play again? (y/n) ")
                if replay == "n":
                    game_on = False
                    break
        
        #Shop
        elif turn_action == "2":
            print("Welcome to the shop!\n")
            
            in_shop = True
            while in_shop:
                shop = Shop([("Leather Tunic", 20), ("Iron Shard", 50), ("Crystal Shard", 200)])
                shop_action = input("What would you like to do?\n1. Buy item\n2. See inventory\n3. Exit\nYour choice: ")
                print("\n")
                if shop_action == "1":
                    shop.display_items(player)
                    item_number = int(input("Which item would you like to buy? "))
                    shop.buy_item(item_number, player)
                elif shop_action == "2":
                    print("Your inventory:")
                    for i, item in enumerate(player.inventory, start=1):
                        print(f"{i}. {item}")
                    print("\n")
                elif shop_action == "3":
                    in_shop = False
                    
        #Inn
        elif turn_action == "3":
            print("Welcome to the inn!\n")
            inn_action = input("What would you like to do?\n1. Rest\n2. Exit\nYour choice: ")
            # print("\n")
            if inn_action == "1":
                player.rest()
                print("Thank you for visiting, you are fully rested!")
                print(f"Your health is now {player.health}!\n")
                player.money -= 10
            elif inn_action == "2":
                pass
            
        #Forge
        elif turn_action == "4":
            forge = Forge(player)
            print("Welcome to the forge!\n")
            forge_action = input("What would you like to do?\n1. Craft weapon\n2. Craft Armour\n3. Exit\nYour choice: ")
            print("\n")
            if forge_action == "1":
                forge.craft_weapon(player)
            elif forge_action == "2":
                forge.craft_armour(player)
            elif forge_action == "3":
                pass
        
        #Summon Dragon
        elif turn_action == "5":
            if player.inventory.count("Dragon Scale") >= 4: 
                dragon = Dragon()
                result = battle(player, dragon)
                if result == "dead":
                    player_alive = False
                    replay = input("Would you like to play again? (y/n) ")
                    if replay == "n":
                        game_on = False
                        break
                else:
                    print("You defeated the Dragon!\n")
                    print("You have won the game!\n")
                    player_alive = False
                    replay = input("Would you like to play again? (y/n) ")
                    if replay == "n":
                        game_on = False
                        break
            else:
                print("You need 4 Dragon Scales to challenge the boss.")
                
        # Save game
        elif turn_action == "6":
            player.save_to_json()
            print("Game saved.\n")
            continue
       
        # Load game
        elif turn_action == "7":
            load_result = player.load_from_json()
            if load_result == "successfull":
                print("Game loaded.\n")
                continue
            continue
        
        