#Nolan Jacob
#11/18/24
#P5HW
#Creating a game in python

#import libraries
import random
import time

#user chooses a pokemon to use in battle
def character_choice():
    print("Choices: ")
    print("Charizard")
    print("Blastoise")
    print("Venusaur")
    name = input("Please select a Pokemon to use in battle: ").lower()

    while name != "charizard" and name != "blastoise" and name != "venusaur":
            print("Please select one of the available Pokemon")
            name = input("Please select a Pokemon")
    
    if name == "charizard":
        name = "Charizard"
        character = {
            "name" : name,
            "health" : 170,
            "attack" : 90,
            "defence" : 70}

    elif name == "blastoise":
        name = "Blastoise"
        character = {
            "name" : name,
            "health" : 210,
            "attack" : 70,
            "defence" : 85}

    elif name == "venusaur":
        name = "Venusaur"
        character = {
            "name" : name,
            "health" : 250,
            "attack" : 60,
            "defence" : 95}

    print(character)
    return character

#User chooses a pokemon to fight
def enemy_choice():
    rng = random.randint(1,3)
    
    if rng == 1:
        name = "Charizard"
        enemy = {
            "name" : name,
            "health" : 170,
            "attack" : 90,
            "defence" : 70}

    elif rng == 2:
        name = "Blastoise"
        enemy = {
            "name" : name,
            "health" : 210,
            "attack" : 70,
            "defence" : 85}

    elif rng == 3:
        name = "Venusaur"
        enemy = {
            "name" : name,
            "health" : 250,
            "attack" : 60,
            "defence" : 95}

    print(f"A wild {enemy['name']} appeared")
    return enemy


def display_character(character):
    for key, value in character.items():
        print(f"{key}: {value}")
    print()

#user chooses how to attack enemy
def user_turn(attacker, victim):
    """
    print(f"{attacker['name']} is attacking {victim['name']}!!!!")
    damage = random.randint(0, attacker['attack'])
    victim['health'] -= damage
    """
    
    if attacker['name'] == "Charizard":
        print("Moves:")
        print("Flamethrower")
        print("Scratch")
        print("Dragon Tail")
        print("Use a Potion")
        print()
        
    elif attacker['name'] == "Blastoise":
        print("Moves:")
        print("Hydro Pump")
        print("Aqua Tail")
        print("Rapid Spin")
        print("Use a Potion")
        print()
        
    elif attacker['name'] == "Venusaur":
        print("Moves:")
        print("Power Whip")
        print("Razor Leaf")
        print("Take Down")
        print("Use a Potion")
        print()
        
    user_move = input("Select a move to use. ").lower()
    print()
    
    if user_move == "flamethrower":
        print(f"{attacker['name']} used Flamethrower")
        accuracy = random.randint(0,100)
        
        if accuracy < 10:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(25, attacker['attack']) + 70 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(25, attacker['attack']) + 70 - victim['defence']

    if user_move == "scratch":
        print(f"{attacker['name']} used Scratch")
        accuracy = random.randint(0,100)
        
        if accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(55, attacker['attack']) + 40 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(55, attacker['attack']) + 40 - victim['defence']
    

    if user_move == "dragon tail":
        print(f"{attacker['name']} used Dragon Tail")
        accuracy = random.randint(0,100)
        
        if accuracy < 20:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(15, attacker['attack']) + 80 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(15, attacker['attack']) + 80 - victim['defence']


    if user_move == "power whip":
        print(f"{attacker['name']} used Power Whip")
        accuracy = random.randint(0,100)
        
        if accuracy < 25:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(15, attacker['attack']) + 90 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(15, attacker['attack']) + 90 - victim['defence']
    
    if user_move == "razor leaf":
        print(f"{attacker['name']} used Razor leaf")
        accuracy = random.randint(0,100)
        
        if accuracy < 5:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(40, attacker['attack']) + 55 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(40, attacker['attack']) + 55 - victim['defence']

    if user_move == "take down":
        print(f"{attacker['name']} used Take Down")
        accuracy = random.randint(0,100)
        
        if accuracy < 15:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(25, attacker['attack']) + 70 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(25, attacker['attack']) + 70 - victim['defence']

    if user_move == "hydro pump":
        print(f"{attacker['name']} used Hydro Pump")
        accuracy = random.randint(0,100)
        
        if accuracy < 20:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(10, attacker['attack']) + 85 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(10, attacker['attack']) + 85 - victim['defence']


    if user_move == "rapid spin":
        print(f"{attacker['name']} used Rapid Spin")
        accuracy = random.randint(0,100)
            
        if accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(50, attacker['attack']) + 45 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(50, attacker['attack']) + 45 - victim['defence']

    
    if user_move == "aqua tail":
        print(f"{attacker['name']} used Aqua Tail")
        accuracy = random.randint(0,100)
        
        if accuracy < 15:
            damage = "miss"
            
        elif accuracy > 98:
            print("A Critical Hit!")
            damage = random.randint(25, attacker['attack']) + 80 - victim['defence']
            damage = damage * 2
            victim['health'] -= damage
            
        else:
            damage = random.randint(25, attacker['attack']) + 80 - victim['defence']


    if user_move == "use a potion":
        print(f"You used a potion.")
        attacker['health'] += 100

    else:
        pass

    print()
    time.sleep(1)
    
    if user_move == "use a potion":
        print(f"{attacker['name']} healed for 100 hp.")

    elif damage == "miss":
        print("But it missed")

    else:
        print(f"{attacker['name']} did {damage} damage to {victim['name']}")
        victim['health'] -= damage
    return victim

#enemy attacks player
def enemy_turn(attacker, victim):
    if attacker['name'] == "Charizard":
        enemy_move = random.randint(1,3)
        
        if enemy_move == 1:
            print(f"{attacker['name']} used Flamethrower")
            accuracy = random.randint(0,100)
            if accuracy < 10:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(25, attacker['attack']) + 70 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(25, attacker['attack']) + 70 - victim['defence']

        if enemy_move == 2:
            print(f"{attacker['name']} used Scratch")
            accuracy = random.randint(0,100)
            
            if accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(55, attacker['attack']) + 40 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(55, attacker['attack']) + 40 - victim['defence']
        

        if enemy_move == 3:
            print(f"{attacker['name']} used Dragon Tail")
            accuracy = random.randint(0,100)
            
            if accuracy < 20:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(15, attacker['attack']) + 80 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(15, attacker['attack']) + 80 - victim['defence']

    elif attacker['name'] == "Venusaur":
        enemy_move = random.randint(1,3)
        
        if enemy_move == 1:
            print(f"{attacker['name']} used Power Whip")
            accuracy = random.randint(0,100)
            
            if accuracy < 25:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(15, attacker['attack']) + 90 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(15, attacker['attack']) + 90 - victim['defence']
        
        if enemy_move == 2:
            print(f"{attacker['name']} used Razor leaf")
            accuracy = random.randint(0,100)
            
            if accuracy < 5:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(40, attacker['attack']) + 55 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(40, attacker['attack']) + 55 - victim['defence']

        if enemy_move == 3:
            print(f"{attacker['name']} used Take Down")
            accuracy = random.randint(0,100)
            
            if accuracy < 15:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(25, attacker['attack']) + 70 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(25, attacker['attack']) + 70 - victim['defence']


    elif attacker['name'] == "Blastoise":
        enemy_move = random.randint(1,3)
        
        if enemy_move == 1:
            print(f"{attacker['name']} used Hydro Pump")
            accuracy = random.randint(0,100)
            
            if accuracy < 20:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(10, attacker['attack']) + 85 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(10, attacker['attack']) + 85 - victim['defence']


        if enemy_move == 2:
            print(f"{attacker['name']} used Rapid Spin")
            accuracy = random.randint(0,100)
                
            if accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(50, attacker['attack']) + 45 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(50, attacker['attack']) + 45 - victim['defence']

        
        if enemy_move == 3:
            print(f"{attacker['name']} used Aqua Tail")
            accuracy = random.randint(0,100)
            
            if accuracy < 15:
                damage = "miss"
                
            elif accuracy > 98:
                print("A Critical Hit!")
                damage = random.randint(25, attacker['attack']) + 80 - victim['defence']
                damage = damage * 2
                victim['health'] -= damage
                
            else:
                damage = random.randint(25, attacker['attack']) + 80 - victim['defence']

    print()
    time.sleep(1)
    
    if damage == "miss":
        print("But it missed")

    else:
        print(f"{attacker['name']} did {damage} damage to {victim['name']}")
        victim['health'] -= damage
    return victim


def main():
    print("Game is starting... ")
    play_game = "yes"

    while play_game == "yes":
        print("\n\n\n")
        #choose characters to use
        character = character_choice()
        print()
        time.sleep(1)

        #random enemy is chosen
        enemy = enemy_choice()
        print()
        time.sleep(1)

        #display both characters
        display_character(character)
        print()
        display_character(enemy)
        time.sleep(1)
        
        #simulate a battle
        while character['health'] > 0 and enemy['health'] > 0:
            enemy = user_turn(character, enemy)
            print()

            print("---Enemy---")
            display_character(enemy)
            print()
            print("---You---")
            display_character(character)
            time.sleep(3)

            character = enemy_turn(enemy, character)
            print()

            print("---Enemy---")
            display_character(enemy)
            print()
            print("---You---")
            display_character(character)
            time.sleep(3)

        #display who won the battle
        if character['health'] <= 0 and enemy['health'] <= 0:
            print("A Double KO!!")
            print("The battle is a draw")

        elif character['health'] > 0 and enemy['health'] <= 0:
            print(f"{enemy['name']} fainted")
            print("You Win The Battle")

        elif character['health'] <= 0 and enemy['health'] > 0:
            print(f"{character['name']} fainted")
            print("You Lost The Battle")

        print()
        play_game = input("Would you like to play again? ")
    
#Call the main
if __name__ == "__main__":
    main()
