from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Represents a character in the game with a name, maximum health points (HP),
    and current HP. This abstract base class provides common functionality
    for all game entities, such as taking damage, healing, and displaying status.

    Attributes:
        name (str): The name of the entity.
        max_hp (int): The maximum health points of the entity.
        hp (int): The current health points of the entity.
    """

    def __init__(self, name, max_hp):
        """
        Initializes a new entity with the given name and maximum HP.
        Sets the entity's current HP to its maximum HP.

        Args:
            name (str): The name of the entity.
            max_hp (int): The maximum health points of the entity.
        """
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp

    def take_damage(self, dmg):
        """
        Reduces the entity's current HP by the given damage amount.
        Ensures that HP does not drop below zero.

        Args:
            dmg (int): The amount of damage to be taken.
        """
        self.hp = max(0, self.hp - dmg)  # HP cannot fall below zero.

    def heal(self):
        """
        Restores the entity's current HP to the maximum HP.
        """
        self.hp = self.max_hp  # Fully restore health to max HP.

    @abstractmethod
    def attack(self, entity):
        """
        Abstract method for attacking another entity. This method should be
        overridden by subclasses to implement specific attack behavior.

        Args:
            entity (Entity): The entity to be attacked.
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the entity, displaying its name
        and current HP status.

        Returns:
            str: A formatted string showing the entity's name and HP.
        """
        return f"{self.name}\nHP: {self.hp}/{self.max_hp}"
