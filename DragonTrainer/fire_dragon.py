from dragon import Dragon
from fire import Fire
import random


class FireDragon(Dragon, Fire):
    """
    Represents a Fire Dragon with fire-based special attacks.

    Inherits from both Dragon and Fire classes, combining the dragon's
    general attributes with fire-specific special attack abilities.
    """

    def __init__(self):
        """
        Initializes a Fire Dragon with a specific name, health points, and number of special attacks.

        The Fire Dragon is named 'Gronkle', has 15 health points, and starts with 3 special attacks.
        """
        super().__init__("Gronkle", 15, 3)  # Initialize with name "Gronkle", 15 HP, and 3 special attacks

    def special_attack(self, opponent):
        """
        Executes one of the fire-based special attacks, chosen at random.

        The Fire Dragon can either use a fireblast or a fireball, with the specific attack
        being randomly selected.

        Parameters:
        ----------
        opponent : Entity
            The opponent (e.g., hero) that the Fire Dragon is attacking.

        Returns:
        -------
        str
            A description of the chosen attack and the damage dealt.
        """
        # Randomly choose between the fireblast and fireball attacks and execute it
        return random.choice([self.fireblast, self.fireball])(opponent)
