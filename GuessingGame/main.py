# Names: Krrish Kohli, Nadhirah Michael-Ho, Nathan Nguyen
# Date: 08/27/2024
# Description: Makes the user guess a randomly generated number by the computer.
import check_input
import random

# Random Number:
    # 1. Generates a random number in the range 1-100 (inclusive).
    # 2. Random number is only generated once at the beginning of the program.
def main():
    random_number = random.randint(1,100)
    guessed_number = check_input.get_int_range("I’m thinking of a number. Make a guess (1-100): ", 1, 100)
    tries = 1
    # Checks:
        # 1. Uses if statements to check if the user’s guess is too high or too low.
        # 2. Uses a while loop that repeats until the user’s guess is correct.
    is_not_right = False
    
    while not is_not_right:
        if guessed_number != random_number:
            if guessed_number > random_number:
                print("Too high! ")
            elif guessed_number < random_number:
                print("Too low! ")
            
    # Validity:
        # 1. Always checks that the user’s guess is a valid integer within the range 1-100 (inclusive).
        # 2. Displays an error message if the user’s guess is invalid and does not increment counter.
            tries += 1
            guessed_number = check_input.get_int_range("Guess again (1-100): ", 1, 100)
        
        else:
            print(f"Correct! You got it in {tries} tries.")
            is_not_right = True

main()
