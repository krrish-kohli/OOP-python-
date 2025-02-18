class Map:
    """Singleton class representing the dungeon map."""
    _instance = None  # Class variable to hold the single instance of Map

    def __new__(cls):
        """Create a new instance of the Map class if it doesn't exist."""
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)  # Create a new instance
        return cls._instance  # Return the existing instance if it exists

    def __init__(self):
        """Initialize the map from a text file and set up the revealed areas."""
        with open("map-1.txt") as file:  # Load the map from 'map-1.txt'
            self.map = [list(line.strip()) for line in file]  # Read each line and store it as a list of characters
        self.revealed = [[False] * len(row) for row in self.map]  # Initialize the revealed map with False values

    def __getitem__(self, row):
        """Allow access to rows of the map using indexing."""
        return self.map[row]  # Return the specified row of the map

    def __len__(self):
        """Return the number of rows in the map."""
        return len(self.map)  # Return the total number of rows in the map

    def show_map(self, loc):
        """Returns a string representation of the map with the hero's location.

        Revealed areas are shown with their actual map content, unrevealed areas are shown as 'x',
        and the hero's location is marked with '*'.

        Args:
            loc (tuple): A tuple representing the (row, column) coordinates of the hero's location.

        Returns:
            str: A formatted string representing the current state of the map.
        """
        output = ""  # Initialize an empty string to build the map representation
        for r in range(len(self.map)):  # Iterate through each row
            for c in range(len(self.map[r])):  # Iterate through each column in the current row
                if (r, c) == loc:  # Check if the current position is where the hero is located
                    output += "* "  # Mark hero's position with '*'
                elif self.revealed[r][c]:  # Check if the current map position has been revealed
                    output += f"{self.map[r][c]} "  # Show the actual map character
                else:
                    output += "x "  # Mark unrevealed areas with 'x'
            output += "\n"  # Move to the next line after finishing a row
        return output  # Return the constructed string representation of the map

    def reveal(self, loc):
        """Reveal the area of the map at the specified location.

        Args:
            loc (tuple): A tuple representing the (row, column) coordinates to reveal.
        """
        self.revealed[loc[0]][loc[1]] = True  # Set the revealed status of the specified location to True

    def remove_at_loc(self, loc):
        """Remove an item from the map at the specified location.

        Args:
            loc (tuple): A tuple representing the (row, column) coordinates of the item to remove.
        """
        self.map[loc[0]][loc[1]] = 'n'  # Replace the item at the specified location with 'n'
