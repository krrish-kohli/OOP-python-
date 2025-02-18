import random


class Die:
    """Represents a single die with a certain number of sides and a current value."""

    def __init__(self, sides=6):
        """Initializes the die with a number of sides and sets its value to a random roll."""
        self.sides = sides
        self.value = self.roll()

    def roll(self):
        """Generates a random number between 1 and the number of sides."""
        self.value = random.randint(1, self.sides)
        return self.value

    def __str__(self):
        """Returns the Die's value as a string."""
        return str(self.value)

    def __lt__(self, other):
        """Checks if the value of this die is less than the value of another die."""
        return self.value < other.value

    def __eq__(self, other):
        """Checks if the value of this die is equal to the value of another die."""
        return self.value == other.value

    def __sub__(self, other):
        """Returns the difference between this die's value and another die's value."""
        return self.value - other.value
