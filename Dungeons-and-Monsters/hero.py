import random
from entity import Entity


class Hero(Entity):
    """
    The hero character controlled by the user, which can move through
    the game map and attack enemies. The hero has a starting position
    at the top-left corner of the map and can move in four directions
    (north, south, east, and west), as long as the movement is within bounds.

    Attributes:
        name (str): The name of the hero.
        max_hp (int): The maximum health points of the hero, inherited from Entity.
        hp (int): The current health points of the hero.
        row (int): The current row position of the hero on the game map.
        col (int): The current column position of the hero on the game map.
    """

    def __init__(self, name):
        """
        Initializes the hero with a name, maximum HP of 25, and
        starting position at the top-left corner of the map (0, 0).

        Args:
            name (str): The name of the hero.
        """
        super().__init__(name, 25)
        self.row = 0
        self.col = 0

    def attack(self, entity):
        """
        Hero attacks an enemy entity with a random damage value between 2 and 5.
        Reduces the enemy's HP by the damage amount.

        Args:
            entity (Entity): The enemy entity being attacked.

        Returns:
            str: A message describing the attack and the damage dealt.
        """
        dmg = random.randint(2, 5)  # Randomize damage between 2 and 5
        entity.take_damage(dmg)
        return f"{self.name} attacks {entity.name} for {dmg} damage."

    def go_north(self, game_map):
        """
        Moves the hero north (up one row) if within map bounds.

        Args:
            game_map (Map): The game map used to check boundaries.

        Returns:
            str: The encounter symbol at the new location, or 'o' if out of bounds.
        """
        if self.row > 0:  # Check if within bounds
            self.row -= 1
            return game_map[self.row][self.col]
        else:
            return 'o'

    def go_south(self, game_map):
        """
        Moves the hero south (down one row) if within map bounds.

        Args:
            game_map (Map): The game map used to check boundaries.

        Returns:
            str: The encounter symbol at the new location, or 'o' if out of bounds.
        """
        if self.row < len(game_map) - 1:  # Check if within bounds
            self.row += 1
            return game_map[self.row][self.col]
        else:
            return 'o'

    def go_east(self, game_map):
        """
        Moves the hero east (right one column) if within map bounds.

        Args:
            game_map (Map): The game map used to check boundaries.

        Returns:
            str: The encounter symbol at the new location, or 'o' if out of bounds.
        """
        if self.col < len(game_map[0]) - 1:  # Check if within bounds
            self.col += 1
            return game_map[self.row][self.col]
        else:
            return 'o'

    def go_west(self, game_map):
        """
        Moves the hero west (left one column) if within map bounds.

        Args:
            game_map (Map): The game map used to check boundaries.

        Returns:
            str: The encounter symbol at the new location, or 'o' if out of bounds.
        """
        if self.col > 0:  # Check if within bounds
            self.col -= 1
            return game_map[self.row][self.col]
        else:
            return 'o'
