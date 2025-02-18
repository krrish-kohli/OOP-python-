# Names: Kareem Fardoun, Krrish Kohli
# Date: 10/03/2024
# Description: A dice game that awards the user points for getting a pair, three-of-a-kind, or a series by rolling three dices.

from player import Player
from check_input import get_yes_no


def take_turn(player):
    """Handles one turn of the game; rolls the dice, checks for win conditions, and updates players' points."""
    player.roll_dice()
    print(player)

    three_of_a_kind = player.has_three_of_a_kind()

    pair = player.has_pair() if not three_of_a_kind else False
    series = player.has_series() if not three_of_a_kind else False

    # Checks for three of a kind first to avoid awarding points for both pair and three-of-a-kind
    if three_of_a_kind:
        print("You got 3 of a kind!")
    elif pair:
        print("You got a pair!")
    # Checking for a series
    elif series:
        print("You got a series of 3!")
    # If player didn't get anything, then printing "Aww. Too Bad."
    else:
        print("Aww. Too Bad.")

    # Displaying the current score
    print(f"Score = {player.get_points()}")


def main():
    """Main function to run the Yahtzee game until the player chooses to quit."""
    print("-Yahtzee-\n")
    player = Player()

    while True:
        take_turn(player)
        if not get_yes_no("Play again? (Y/N): "):
            break

    print(f"Game Over.\nFinal Score = {player.get_points()}")


if __name__ == "__main__":
    main()
