import random
from entity import Entity


class Enemy(Entity):
    """Represents an enemy character that the hero may encounter in the dungeon."""

    def __init__(self):
        """Initializes an enemy with a random name and maximum health points (HP).

        The enemy's name is chosen randomly from a predefined list and its
        maximum HP is assigned a random value between 4 and 8.
        """
        names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]  # List of possible enemy names
        name = random.choice(names)  # Select a random name for the enemy
        max_hp = random.randint(4, 8)  # Assign a random maximum HP between 4 and 8
        super().__init__(name, max_hp)  # Initialize the parent class (Entity) with the chosen name and max HP

    def attack(self, entity):
        """Causes the enemy to attack a target entity (e.g., the hero).

        The damage dealt is a random integer between 1 and 4. After dealing
        damage, it also returns a message describing the attack.

        Args:
            entity (Entity): The target entity that the enemy is attacking.

        Returns:
            str: A message indicating the attack details.
        """
        dmg = random.randint(1, 4)  # Calculate random damage between 1 and 4
        entity.take_damage(dmg)  # Inflict damage on the target entity
        return f"{self.name} attacks {entity.name} for {dmg} damage."  # Return a message describing the attack
