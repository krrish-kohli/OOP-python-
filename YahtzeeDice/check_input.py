def get_yes_no(prompt):
    """Prompts the user for a yes or no response to ensure valid input."""
    while True:
        response = input(prompt).lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("Invalid input - should be a 'Yes' or 'No'.")
