from dragon import Dragon
from flying import Flying
import random


class FlyingDragon(Dragon, Flying):
    """
    Represents a Flying Dragon with flying-based special attacks.

    Inherits from both Dragon and Flying classes, giving the dragon flying-related
    special abilities in addition to basic dragon attacks.
    """

    def __init__(self):
        """
        Initializes a Flying Dragon with a specific name, health points, and number of special attacks.

        The Flying Dragon is named 'Timberjack', has 10 health points, and starts with 3 special attacks.
        """
        super().__init__("Timberjack", 10, 3)  # Initialize with name "Timberjack", 10 HP, and 3 special attacks

    def special_attack(self, opponent):
        """
        Executes one of the flying-based special attacks, chosen at random.

        The Flying Dragon can either use swoop or windblast, with the specific attack
        being randomly selected.

        Parameters:
        ----------
        opponent : Entity
            The opponent (e.g., hero) that the Flying Dragon is attacking.

        Returns:
        -------
        str
            A description of the chosen attack and the damage dealt.
        """
        # Randomly choose between the swoop and windblast attacks and execute it
        return random.choice([self.swoop, self.windblast])(opponent)
