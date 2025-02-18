# Names: Kareem Fardoun, Krrish Kohli
# Date: 9/3/2024
# Description: This program will prompt the user to play a game of rock, paper, scissors with the computer. Starting with a menu that allows the user to choose to play, see the currect score, or quit. And continuing until the user quits.

import random

def weapon_menu():
        """Asks the user to input their choice: (R)ock, (P)aper, (S)cissors, or (B)ack. Checks user input for validity and then returns the inputted value."""
        while True:
            print("\nChoose your weapon: \nR. Rock \nP. Paper \nS. Scissors \nB. Back")
            choice = input().upper()
            if choice == 'R' or choice == 'P' or choice == 'S' or choice == 'B':
                return choice
            else:
                print("Invalid input. Please choose R, P, S, or B.")

def comp_weapon():
    """Randomly chooses the computer’s throw and returns an 'R', 'P', or 'S'."""
    comp_number = random.randint(0, 2)
    if comp_number == 0:
        return "Rock"
    elif comp_number == 1:
        return "Paper"
    else:
        return "Scissors"

def find_winner(player, comp):
    """Compares the two weapons and chooses the winner."""
    if player == 'R':
         player = 'Rock'
    elif player == 'P':
        player = 'Paper'
    else:
        player = 'Scissors'
    print(f"\nYou chose {player}")
    print(f"Computer chose {comp}")

    if player == comp:
        print("Tie")
        return 0
    elif (player == 'Rock' and comp == 'Scissors') or \
         (player == 'Scissors' and comp == 'Paper') or \
         (player == 'Paper' and comp == 'Rock'):
        print("Player wins")
        return 1
    else:
        print("Computer wins")
        return 2
        
def display_scores(player, comp):
    """Displays the current scores of the player and the computer."""
    print(f"\nPlayer = {player}")
    print(f"Computer = {comp}")

def main():
    player_score = 0
    comp_score = 0

    while True:
        print("\nRPS Menu: \n1. Play game \n2. Show Score \n3. Quit")
        choice = input()

        if choice == '1':
            while True:
                player_weapon = weapon_menu()
                if player_weapon == 'B':
                    break
                comp_weapon_choice = comp_weapon()
                winner = find_winner(player_weapon, comp_weapon_choice)
                if winner == 1:
                    player_score += 1
                elif winner == 2:
                    comp_score += 1

        elif choice == '2':
            display_scores(player_score, comp_score)

        elif choice == '3':
            print("\nFinal Score:")
            display_scores(player_score, comp_score)
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

main()
