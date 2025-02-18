# Names: Kareem Fardoun, Krrish Kohli
# Date: 10/31/2024
# Description: This project is a text-based dungeon adventure game where players assume the role of a hero navigating a dungeon map, battling enemies, discovering items, and making choices that affect their journey and survival.

import random
from hero import Hero
from enemy import Enemy
from map import Map
from check_input import get_int_range


def main():
    """Main function to run the dungeon adventure game."""
    name = input("What is your name, traveler? ").strip()  # Prompt the user for their name
    hero = Hero(name)  # Create a Hero object with the entered name
    game_map = Map()  # Create an instance of the Map

    while True:
        # Display hero's status and the map
        print(hero)  # Print the hero's current status
        print(game_map.show_map((hero.row, hero.col)))  # Display the map showing the hero's location

        # Prompt user for movement choice
        choice = get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: ", 1, 5)

        if choice == 5:
            print("Goodbye, brave adventurer!")  # Exit message
            break  # Exit the game loop

        # Define movement directions and update location
        directions = {1: hero.go_north, 2: hero.go_south, 3: hero.go_east, 4: hero.go_west}
        encounter = directions[choice](game_map)  # Move in the chosen direction
        game_map.reveal((hero.row, hero.col))  # Reveal the area the hero just moved to

        # Handle encounters based on the map character
        if encounter == 'm':  # Encounter an enemy
            enemy = Enemy()  # Create a new Enemy object
            print(f"You encounter a {enemy.name}\nHP: {enemy.hp}/{enemy.max_hp}")  # Display enemy info
            while enemy.hp > 0 and hero.hp > 0:  # Battle loop
                action = get_int_range(f"1. Attack {enemy.name}\n2. Run Away\nEnter choice: ", 1, 2)
                if action == 1:  # If the hero chooses to attack
                    print(hero.attack(enemy))  # Hero attacks enemy
                    if enemy.hp > 0:  # If the enemy is still alive
                        print(enemy.attack(hero))  # Enemy retaliates
                else:  # If the hero chooses to run away
                    random_directions = [hero.go_north, hero.go_south, hero.go_east, hero.go_west]
                    random.shuffle(random_directions)  # Randomize movement direction
                    for move in random_directions:
                        random_encounter = move(game_map)  # Attempt to move in a random direction
                        if random_encounter != 'o':  # Only move if within bounds
                            game_map.reveal((hero.row, hero.col))  # Reveal new area
                            print("You ran away to a new location!")  # Inform the player of escape
                            break  # Exit the loop after moving
                    break  # Exit the battle loop after trying to run
            if enemy.hp <= 0:  # Check if the enemy is defeated
                print(f"You have slain the {enemy.name}")  # Victory message
                game_map.remove_at_loc((hero.row, hero.col))  # Remove the enemy from the map
            if hero.hp <= 0:  # Check if the hero is defeated
                print("You have fallen. Game over.")  # Game over message
                break  # Exit the game loop
        elif encounter == 'o':  # Encounter an obstacle
            print("You cannot go that way...")  # Inform the player of an invalid move
        elif encounter == 'n':  # Encounter nothing
            print("There is nothing here...")  # Inform the player of an empty space
        elif encounter == 's':  # Encounter the start
            print("You wound up back at the start of the dungeon.")  # Inform the player of the starting point
        elif encounter == 'i':  # Encounter an item
            if hero.hp == hero.max_hp:  # Check if the hero's health is full
                print("You found a health potion but are already at full health.")  # No need for healing
            else:
                print("You found a health potion! You drink it to restore your health.")  # Healing message
                hero.heal()  # Heal the hero
            game_map.remove_at_loc((hero.row, hero.col))  # Remove the item from the map
        elif encounter == 'f':  # Encounter the exit
            print("Congratulations! You found the exit and escaped the dungeon.")  # Victory message
            break  # Exit the game loop
        else:  # Any other encounter
            print("You continue on your journey...")  # Continue the journey


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
