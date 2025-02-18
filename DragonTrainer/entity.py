from abc import ABC, abstractmethod


class Entity(ABC):
    """
    Abstract base class representing a general entity (hero/dragon).
    Both heroes and dragons share common attributes like name and health points (HP).

    Attributes:
    ----------
    _name : str
        Name of the entity.
    _max_hp : int
        Maximum health points of the entity.
    _hp : int
        Current health points of the entity.
    """

    def __init__(self, name, max_hp):
        """
        Initializes an entity with a name and maximum health points.

        Parameters:
        ----------
        name : str
            Name of the entity (hero or dragon).
        max_hp : int
            Maximum health points for the entity.
        """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp  # Start with full health

    @property
    def name(self):
        """Returns the name of the entity."""
        return self._name

    @property
    def hp(self):
        """Returns the current health points of the entity."""
        return self._hp

    def take_damage(self, dmg):
        """
        Reduces the entity's health points (HP) based on the damage taken.
        Ensures that the HP does not go below 0.

        Parameters:
        ----------
        dmg : int
            Amount of damage inflicted on the entity.
        """
        self._hp = max(0, self._hp - dmg)  # Prevent HP from going below 0

    def __str__(self):
        """
        String representation of the entity.

        Returns:
        -------
        str
            The entity's name followed by its current HP and maximum HP.
        """
        return f"{self._name}: {self._hp}/{self._max_hp}"

    @abstractmethod
    def basic_attack(self, opponent):
        """
        Abstract method for the basic attack.
        Must be implemented by subclasses (e.g., hero, dragon).

        Parameters:
        ----------
        opponent : Entity
            The entity that will be attacked.
        """
        pass

    @abstractmethod
    def special_attack(self, opponent):
        """
        Abstract method for the special attack.
        Must be implemented by subclasses (e.g., hero, dragon).

        Parameters:
        ----------
        opponent : Entity
            The entity that will be attacked.
        """
        pass
