import random

class Fire:
    """
    Mixin class for fire-based special attacks.

    Provides fire-related abilities to an entity, such as fireblast and fireball.
    These attacks consume special attacks and deal damage to an opponent.
    """

    def fireblast(self, opponent):
        """
        Performs a fireblast attack dealing 5-9 damage if special attacks remain.

        Parameters:
        ----------
        opponent : Entity
            The entity that will be attacked.

        Returns:
        -------
        str
            A message describing the outcome of the fireblast attack.
        """
        if self._special_attacks > 0:
            dmg = random.randint(5, 9)
            opponent.take_damage(dmg)
            self.decrement_special_attacks()
            return f"{self.name} blasts {opponent.name} with fire for {dmg} damage!"
        return f"{self.name} tries to blast fire but is out of fuel."

    def fireball(self, opponent):
        """
        Performs a fireball attack dealing 4-8 damage if special attacks remain.

        Parameters:
        ----------
        opponent : Entity
            The entity that will be attacked.

        Returns:
        -------
        str
            A message describing the outcome of the fireball attack.
        """
        if self._special_attacks > 0:
            dmg = random.randint(4, 8)
            opponent.take_damage(dmg)
            self.decrement_special_attacks()
            return f"{self.name} shoots a fireball at {opponent.name} for {dmg} damage!"
        return f"{self.name} tries to shoot a fireball but is out of fuel."
