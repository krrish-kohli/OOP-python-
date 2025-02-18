import random
from abc import ABC
from entity import Entity


class Dragon(Entity, ABC):
    """
    Represents a dragon character with basic and special attacks, inheriting from Entity.

    Each dragon has a limited number of special attacks in addition to basic attacks.
    """

    def __init__(self, name, max_hp, num_sp):
        """
        Initializes a dragon with a name, maximum health points, and a set number of special attacks.

        Parameters:
        ----------
        name : str
            The name of the dragon.
        max_hp : int
            The maximum health points of the dragon.
        num_sp : int
            The number of special attacks the dragon has.
        """
        super().__init__(name, max_hp)  # Initialize the name and HP from the Entity class
        self._special_attacks = num_sp  # Number of special attacks remaining

    def decrement_special_attacks(self):
        """
        Decrements the number of special attacks the dragon has left.

        Ensures that the number of special attacks doesn't drop below 0.
        """
        self._special_attacks = max(0, self._special_attacks - 1)  # Decrease, but don't go below 0

    def basic_attack(self, opponent):
        """
        Performs a basic tail attack, dealing 3-7 damage to the opponent.

        Parameters:
        ----------
        opponent : Entity
            The opponent (e.g., hero) that the dragon is attacking.

        Returns:
        -------
        str
            A description of the attack and the damage dealt.
        """
        dmg = random.randint(3, 7)  # Damage is randomly selected between 3 and 7
        opponent.take_damage(dmg)  # Inflict the damage on the opponent
        return f"{self.name} smashes {opponent.name} with its tail for {dmg} damage!"

    def __str__(self):
        """
        Returns a string representation of the dragon, including its name, health points,
        and the number of special attacks remaining.

        Returns:
        -------
        str
            A string describing the dragon's current state.
        """
        return super().__str__() + f", Special attacks remaining: {self._special_attacks}"
