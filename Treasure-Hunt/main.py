def read_map(filename):
    """Read the map from a file and return a 2D list"""
    with open(filename, 'r') as file:
        lines = file.readlines()
        map_grid = []
        for line in lines:
            line = line.strip().replace(" ", "")
            map_grid.append(list(line))
    return map_grid


def display_map(map_grid, player):
    """Display the map with the player's current position"""
    for row in range(len(map_grid)):
        for col in range(len(map_grid[0])):
            if [row, col] == player:
                # Display the player's position
                print("P", end=" ")
            else:
                print(map_grid[row][col], end=" ")
        print()
    print()


def move_player(player, direction, upper_bound):
    """Moves the player based on input direction"""
    row, col = player

    # Move up
    if direction == 'W':
        if row > 0:
            player[0] -= 1
        else:
            print("You can't move up, you're at the top!")
    # Move down
    elif direction == 'S':
        if row < upper_bound:
            player[0] += 1
        else:
            print("You can't move down, you're at the bottom!")
    # Move left
    elif direction == 'A':
        if col > 0:
            player[1] -= 1
        else:
            print("You can't move left, you're at the left edge!")
    # Move right
    elif direction == 'D':
        if col < upper_bound:
            player[1] += 1
        else:
            print("You can't move right, you're at the right edge!")
    else:
        print("Invalid move! Please use W, A, S, or D.")

    return player


def count_treasures_traps(map_grid, player, upper_bound):
    """Count treasures and traps surrounding the player"""
    row, col = player
    treasure_count = 0
    trap_count = 0

    # Iterating through surrounding spaces
    # Loop to ensure we don't go beyond the top or bottom boundary of grid
    for r in range(max(0, row - 1), min(upper_bound + 1, row + 2)):
        # Loop to ensure we don't go beyond the left or right boundary of grid
        for c in range(max(0, col - 1), min(upper_bound + 1, col + 2)):
            # Increasing the treasure count if treasure is found
            if map_grid[r][c] == 'T':
                treasure_count += 1
            # Increasing the trap count if trap is found
            elif map_grid[r][c] == 'X':
                trap_count += 1

    return treasure_count, trap_count


def main():
    # Reading the file and returning a 2D list
    map_grid = read_map('map.txt')
    # Player starts at upper left corner (0, 0)
    player = [0, 0]
    # Displayed map for the player
    display_grid = [['.' for _ in range(7)] for _ in range(7)]
    # Initialising the variables
    treasures_found = 0
    total_treasures = 7
    upper_bound = 6
    game_over = False

    while not game_over:
        # Display player's map
        display_map(display_grid, player)
        print(f"Treasures found: {treasures_found}/{total_treasures}")

        move = input("Enter move (W/A/S/D), look around (L), or quit (Q): ").upper()
        if move == 'Q':
            print("You quit the game.")
            break
        elif move in ['W', 'A', 'S', 'D']:
            # Move player in the direction
            player = move_player(player, move, upper_bound)

            # Check what's at the player's location in the hidden map
            current_position = map_grid[player[0]][player[1]]
            # If player found a treasure
            if current_position == 'T':
                print("You found a treasure!")
                display_grid[player[0]][player[1]] = 'T'
                treasures_found += 1
                # If player found all the treasures
                if treasures_found == total_treasures:
                    print("Congratulations! You've found all the treasures!")
                    game_over = True
            # If player found a trap
            elif current_position == 'X':
                print("Oh no! You hit a trap! Game over.")
                game_over = True
            # If the space is empty
            else:
                display_grid[player[0]][player[1]] = '.'

        elif move == 'L':
            # Get the count of treasures and traps surrounding the player
            treasures, traps = count_treasures_traps(map_grid, player, upper_bound)

            # Display the number of treasures and traps to the player
            print(f"There are {treasures} treasure(s) and {traps} trap(s) nearby.")

            # Mark the number of traps at the player's current position on the player's map
            if display_grid[player[0]][player[1]] != 'T':
                display_grid[player[0]][player[1]] = str(traps)

        print("Game Over!")


main()
