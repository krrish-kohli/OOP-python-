# Name: Krrish Kohli, Kareem Fardoun
# Date: 09/12/2024
# Description: This is a game in which we guess a 5-letter word in a limited number of chances.

import random
import check_input
from dictionary import words


def display_gallows(num_incorrect):
    """
    Function to display the gallows based on the number of incorrect guesses
    """
    
    # List of different stages of the hangman based on the number of incorrect guesses
    stages = [
        '''
        =======
        ||/   |
        ||    
        ||    
        ||    
        ||
        ''',  
        '''
        =======
        ||/   |
        ||    o
        ||    
        ||    
        ||
        ''',  
        '''
        =======
        ||/   |
        ||    o
        ||    |
        ||    
        ||
        ''',  
        '''
        =======
        ||/   |
        ||    o
        ||    |
        ||   /
        ||
        ''',  
        '''
        =======
        ||/   |
        ||    o
        ||    |
        ||   / \\
        ||
        ''',  
        '''
        =======
        ||/   |
        ||    o
        ||   /|
        ||   / \\
        ||
        ''',  
        '''
        =======
        ||/   |
        ||    o
        ||   /|\\
        ||   / \\
        ||
        '''  
    ]

    # Display the appropriate stage based on incorrect guesses
    print(stages[num_incorrect])


def display_letters(letters):
    """
    Function to display letters in a formatted manner (letters separated by spaces)
    """

    # Joins the list of letters with spaces between them and prints them
    print(' '.join(letters))


def get_letters_remaining(incorrect, correct):
    """
    Function to return remaining letters that haven't been guessed yet
    """
    all_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # Combine incorrect and correct guesses into one list
    guessed_letters = incorrect + correct
    # Create a new list of letters that haven't been guessed yet
    remaining_letters = [letter for letter in all_letters if letter not in guessed_letters]
    # Sort the remaining letters alphabetically
    remaining_letters.sort()
    
    return remaining_letters


def main():
    # Start an infinite loop for the game (until the user decides to quit)
    while True:
        # Choose a random word from the words list and convert it to uppercase
        word_to_guess = random.choice([word.upper() for word in words])

         # List to store the correct guesses (5 underscores for a 5-letter word)
        correct_guesses = ['_'] * 5
        # List to store incorrect guesses
        incorrect_guesses = []
        num_correct = 0
        num_incorrect = 0

        print("\nWelcome to Hangman!")

        # Main game loop that runs until the player wins or loses
        while num_correct < 5 and num_incorrect < 6:
            display_gallows(num_incorrect)
            print("Current word:", end=" ")
            # Show the current state of the guessed word (with blanks for missing letters)
            display_letters(correct_guesses)
            print("Incorrect guesses:", end=" ")
            display_letters(incorrect_guesses)
            # Get and display the list of remaining letters that haven't been guessed yet
            remaining_letters = get_letters_remaining(incorrect_guesses, correct_guesses)
            print("Letters remaining:", end=" ")
            # Show the remaining available letters
            display_letters(remaining_letters)

            # Prompt the user to guess a letter
            guess = input("Enter a letter: ").upper()

            # Validate the user's input
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter from A-Z.")
                continue

            # Check if the guessed letter has already been guessed (either correct or incorrect)
            if guess in incorrect_guesses or guess in correct_guesses:
                print("You already guessed that letter.")
                continue

            # If the guessed letter is in the word
            if guess in word_to_guess:
                # Update the correct guesses list with the guessed letter in the correct positions
                for i in range(5):
                    # Check if the guessed letter is in the word
                    if word_to_guess[i] == guess and correct_guesses[i] == "_":
                        correct_guesses[i] = guess
                        num_correct += 1

                 # If the word is not fully guessed, print "Correct!"
                if num_correct != 5:
                    print("Correct!")

            # If the guessed letter is not in the word
            else:
                # Notify the player that the guess was incorrect and update the necessary variables.
                print("Incorrect!")
                incorrect_guesses.append(guess)
                # Sort the incorect guesses
                incorrect_guesses.sort()
                num_incorrect += 1

        # End of the game: Determine if the player won or lost

        # If the player has correctly guessed all letters
        if num_correct == 5:
            print("\nYou win!")
        else:
            # Display the full hangman for the losing condition
            display_gallows(6)
            print("\nSorry, you lost! The correct word was:", word_to_guess)

        # Ask if the player wants to play again
        play_again = check_input.get_yes_no("Play again (Y/N)? ")
        if not play_again:
            break


main()
