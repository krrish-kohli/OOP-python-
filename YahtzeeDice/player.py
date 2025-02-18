from die import Die


class Player:
    """Represents a player with three dice and a score, who is capable of detecting pairs, series, and three-of-a-kind."""

    def __init__(self):
        """Constructs and sorts the list of three Die objects and initializes the player’s points to 0"""
        self.dice = sorted([Die() for _ in range(3)])
        self.points = 0

    def get_points(self):
        """Returns the player's points."""
        return self.points

    def roll_dice(self):
        """Calls roll on each of the Die objects in the dice list and sorts the list"""
        for die in self.dice:
            die.roll()
        self.dice.sort()

    def has_pair(self):
        """Checks if the player has a pair of dice with the same value. Increments points by 1."""
        if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2]:
            self.points += 1
            return True
        return False

    def has_three_of_a_kind(self):
        """Checks if the player has three dice with the same value. Increments points by 3"""
        if self.dice[0] == self.dice[1] == self.dice[2]:
            self.points += 3
            return True
        return False

    def has_series(self):
        """Checks if the player has three consecutive dice values. Increments points by 2."""
        if self.dice[1] - self.dice[0] == 1 and self.dice[2] - self.dice[1] == 1:
            self.points += 2
            return True
        return False

    def __str__(self):
        """Returns a string in the format: “D1=2, D2=4, D3=6”."""
        return f"D1={self.dice[0]}, D2={self.dice[1]}, D3={self.dice[2]}"
