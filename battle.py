from entities import *
import random

#Battle function
def battle(player, enemy):
    print(enemy.name + " has appeared!\n")
    #Battle loop
    while player.health > 0 and enemy.health > 0:
        print("Your health: " + str(int(player.health)))
        print("Enemy health: " + str(int(enemy.health)) + "\n")
        turn_action = input("What would you like to do?\n1. Attack\n2. Run\nYour choice: ")
        print()
        #Attack
        if turn_action == "1":
            player.attack(enemy)
            if enemy.health > 0:
                enemy.attack(player)
        #Run
        elif turn_action == "2":
            if random.choice([0,0,1]) == 1:
                print("You ran away!\n")
                return None
            else:
                print("You failed to run away!\n")
                enemy.attack(player)
    
    #Battle result
    if player.health <= 0:
        print("You died!\n")
        return "dead"
    elif enemy.health <= 0:
        print(f"You defeated the {enemy.name}!\n")
        player.gain_experience(enemy.level * 10)
            
    