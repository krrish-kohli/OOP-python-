import random
from entity import Entity


class Hero(Entity):
    """
    Represents the hero character with basic and special attack abilities.

    Inherits from the abstract Entity class and implements the basic and special
    attack methods to allow the hero to deal damage to opponents.
    """

    def basic_attack(self, opponent):
        """
        Performs a basic sword attack on the opponent, dealing 2D6 damage.

        The hero swings their sword, and the damage is calculated by rolling
        two 6-sided dice (2D6). The opponent's health points (HP) are reduced
        by the damage amount.

        Parameters:
        ----------
        opponent : Entity
            The opponent (e.g., dragon) that the hero is attacking.

        Returns:
        -------
        str
            A description of the attack and the damage dealt.
        """
        dmg = random.randint(1, 6) + random.randint(1, 6)  # Damage = 2 rolls of 6-sided dice
        opponent.take_damage(dmg)  # Inflict damage on the opponent
        return f"{self.name} slashes {opponent.name} with their sword for {dmg} damage!"

    def special_attack(self, opponent):
        """
        Performs a special arrow attack on the opponent, dealing 1D12 damage.

        The hero shoots an arrow, and the damage is calculated by rolling
        a 12-sided die (1D12). The opponent's health points (HP) are reduced
        by the damage amount.

        Parameters:
        ----------
        opponent : Entity
            The opponent (e.g., dragon) that the hero is attacking.

        Returns:
        -------
        str
            A description of the attack and the damage dealt.
        """
        dmg = random.randint(1, 12)  # Damage = 1 roll of 12-sided die
        opponent.take_damage(dmg)  # Inflict damage on the opponent
        return f"{self.name} shoots an arrow at {opponent.name} for {dmg} damage!"
