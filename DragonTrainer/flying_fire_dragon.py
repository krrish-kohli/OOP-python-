from dragon import Dragon
from fire import Fire
from flying import Flying
import random


class FlyingFireDragon(Dragon, Fire, Flying):
    """
    Represents a hybrid dragon with both fire-based and flying-based special attacks.

    Inherits from the Dragon, Fire, and Flying classes, allowing the dragon to use a
    combination of fire and flying special abilities.
    """

    def __init__(self):
        """
        Initializes a FlyingFireDragon with a specific name, health points, and number of special attacks.

        The hybrid dragon is named 'Deadly Nadder', has 20 health points, and starts with 2 special attacks.
        """
        super().__init__("Deadly Nadder", 20, 2)  # Initialize with name "Deadly Nadder", 20 HP, and 2 special attacks

    def special_attack(self, opponent):
        """
        Executes a randomly chosen special attack from the four available options: fireblast, fireball, swoop, or windblast.

        The special attack is selected at random from both fire-based and flying-based attacks.

        Parameters:
        ----------
        opponent : Entity
            The opponent (e.g., hero) that the hybrid dragon is attacking.

        Returns:
        -------
        str
            A description of the chosen attack and the damage dealt.
        """
        # Randomly select an attack from fireblast, fireball, swoop, or windblast
        attack_method = random.choice([self.fireblast, self.fireball, self.swoop, self.windblast])
        return attack_method(opponent)  # Execute the chosen attack
