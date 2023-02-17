import numpy as np
# Helper functions for tic-tac-toe
# Assumptions: grid is an 2-dimensional NumPy array with equal sides of length n
# There are 2 players in the game, denoted with +1 and -1
# A win happens when a row, column or diagonal is filled with the same player's marks

def generate_grid(n):
    return np.zeros((n, n), int)

def add_mark(grid, x, y, marker):
    # Check if the grid contains a mark first
    if grid[y, x] != 0:
        return None

    # Add the new mark
    grid_new = grid.copy()
    grid_new[y, x] = marker
    return grid_new

def check_win(grid):
    # Check for rows and columns
    grid_len = len(grid)

    for i in range(grid_len):
        if np.sum(grid[i, :]) == grid_len or np.sum(grid[:, i]) == grid_len:
            return 1
        elif np.sum(grid[i, :]) == -grid_len or np.sum(grid[:, i]) == -grid_len:
            return -1

    # Check for diagonals
    if np.sum(grid.diagonal()) == grid_len or np.sum(np.fliplr(grid).diagonal()) == grid_len:
        return 1
    elif np.sum(grid.diagonal()) == -grid_len or np.sum(np.fliplr(grid).diagonal()) == -grid_len:
        return -1

    # Return false if all checks fail
    return 0
def print_grid(grid):
    # Generate a nice-looking tic tac toe grid based on the internal grid
    print(grid)


grid_size = 3
grid = generate_grid(grid_size)

# Gameplay Loop
for i in range(len(grid) ** 2):
    # Print the current board state
    print_grid(grid)
    print("")

    # Determine current turn
    if i % 2 == 0:
        player = 1
        print("Player 1's turn")
    else:
        player = -1
        print("Player 2's turn")

    # Add a new mark to the grid
    while True:
        # Get x and y coordinates from the player
        try:
            x_input = int(input("X Coordinate:")) - 1
            y_input = int(input("Y Coordinate:")) - 1
        except ValueError:
            print("Invalid input!")
            continue
        except Exception as e:
            print(e)
            continue

        # Verify if input is valid
        if not ((0 <= x_input <= grid_size) or (0 <= y_input <= grid_size)):
            print("Coordinate is not within range!")
            continue

        # Place the mark based on turn order
        new_grid = add_mark(grid, x_input, y_input, player)

        # If mark already in location, try again
        if new_grid is None:
            print("Location already occupied!")
            continue

        # If the position is valid, break the loop
        grid = new_grid
        break

    # Check for a win
    possible_winner = check_win(grid)
    if possible_winner == 1:
        print("Player 1 wins!")
        break
    elif possible_winner == -1:
        print("Player 2 wins!")
        break

else:
    # If no one wins within the gameplay loop, it's a tie
    print("It's a tie!")