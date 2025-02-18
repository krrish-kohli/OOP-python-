# Names: Kareem Fardoun, Krrish Kohli
# Date: 10/24/2024
# Description: A dragon battle game where the user controls a hero to defeat three dragons using basic and special attacks, with each dragon having unique abilities inherited from mixin classes. The game ends when all dragons are defeated or the hero runs out of health.

import random
from hero import Hero
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from flying_fire_dragon import FlyingFireDragon
import check_input


def display_status(hero, dragons):
    """
    Display the status of the hero and the remaining dragons.

    Args:
        hero (Hero): The player's hero object.
        dragons (list): A list of the remaining dragon objects.
    """
    print(f"\n{hero}")
    for i, dragon in enumerate(dragons):
        print(f"{i + 1}. {dragon}")
    print()


def main():
    """
    Main function that controls the game loop. The player will face off against 3 dragons,
    and the game ends either when all dragons are defeated or the hero's HP reaches 0.

    - The player selects a dragon to attack.
    - The player chooses a weapon (Sword or Arrow).
    - The player and dragons take turns attacking until one side is defeated.
    """
    print("What is your name, challenger?")
    hero_name = input()  # Get the player's name input
    hero = Hero(hero_name, 50)  # Initialize the hero with the given name and 50 HP

    # Create a list of dragons for the player to battle
    dragons = [FireDragon(), FlyingDragon(), FlyingFireDragon()]

    print(f"Welcome to dragon training, {hero_name}")
    print("You must defeat 3 dragons.")

    current_dragon = None  # To store the dragon currently being attacked

    # Main game loop: continue while the hero is alive and there are dragons left
    while len(dragons) > 0 and hero.hp > 0:
        display_status(hero, dragons)  # Show current status of hero and dragons

        # If no dragon is currently targeted, ask the player to select one
        if current_dragon is None:
            dragon_choice = check_input.get_int_range("Choose a dragon to attack: ", 1, len(dragons))
            current_dragon = dragons[dragon_choice - 1]  # Set the chosen dragon

        # Ask the player to choose their weapon
        weapon_choice = check_input.get_int_range(
            "Attack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)\nEnter weapon: ", 1, 2)

        # Perform the attack based on the chosen weapon
        if weapon_choice == 1:
            print(hero.basic_attack(current_dragon))  # Sword attack
        else:
            print(hero.special_attack(current_dragon))  # Arrow attack

        # Check if the current dragon has been defeated
        if current_dragon.hp == 0:
            print(f"{current_dragon.name} has been defeated!")
            dragons.remove(current_dragon)  # Remove the defeated dragon from the list
            current_dragon = None  # Reset to allow the player to choose a new dragon

        # If dragons remain, one will randomly attack the hero
        if len(dragons) > 0:
            attacking_dragon = random.choice(dragons)  # Choose a random dragon to attack
            attack_choice = random.choice([attacking_dragon.basic_attack, attacking_dragon.special_attack])
            print(attack_choice(hero))  # Randomly choose a dragon attack

        # Check if the hero has been defeated
        if hero.hp <= 0:
            print("You have been defeated. Better luck next time.")
            break  # End the game loop if the hero's HP is 0

    # If the hero has survived and defeated all dragons, print a victory message
    if hero.hp > 0:
        print("Congratulations! You have defeated all three dragons, you have passed the trials.")


if __name__ == "__main__":
    main()
