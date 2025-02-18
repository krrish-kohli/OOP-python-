import random

class Flying:
    """
    Mixin class for flying-based special attacks.

    Provides flying-related abilities to an entity, such as swoop and windblast.
    These attacks consume special attacks and deal damage to an opponent.
    """

    def swoop(self, opponent):
        """
        Performs a swoop attack dealing 4-8 damage if special attacks remain.

        Parameters:
        ----------
        opponent : Entity
            The entity that will be attacked.

        Returns:
        -------
        str
            A message describing the outcome of the swoop attack.
        """
        if self._special_attacks > 0:
            dmg = random.randint(4, 8)
            opponent.take_damage(dmg)
            self.decrement_special_attacks()
            return f"{self.name} swoops at {opponent.name} for {dmg} damage!"
        return f"{self.name} tries to swoop but is out of energy."

    def windblast(self, opponent):
        """
        Performs a windblast attack dealing 3-7 damage if special attacks remain.

        Parameters:
        ----------
        opponent : Entity
            The entity that will be attacked.

        Returns:
        -------
        str
            A message describing the outcome of the windblast attack.
        """
        if self._special_attacks > 0:
            dmg = random.randint(3, 7)
            opponent.take_damage(dmg)
            self.decrement_special_attacks()
            return f"{self.name} blasts wind at {opponent.name} for {dmg} damage!"
        return f"{self.name} tries to blast wind but is out of energy."
