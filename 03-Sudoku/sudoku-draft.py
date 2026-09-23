# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      Display and 'play' the game of Sudoku without any of the rules.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how I wanted to store save games.
#      I ended up slicing the file name and adding a timestamp.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

import json, datetime

def save_game(filename: str, board: list[list[int]]):
    '''Saves a sudoku game to a json file'''
    # Create data to save
    save_json = {
        "board": board
    }

    # Try saving game
    try:
        with open(filename, "w") as f:
            json.dump(save_json, f)

    # Error occurred while saving
    except Exception as e:
        print(f"Error: {e}")

def load_game(filename: str) -> list[list[int]]:
    '''Loads a sudoku board from a json file'''
    # Input does not include file extension so put it on
    filename += ".json"
    # Try opening file and getting data
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            board = data["board"]
            return board
    # File doesn't exist
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
    # Other error
    except Exception as e:
        print(f"Error: {e}")

def convert_to_coordinate(input: str) -> tuple[int, int]:
    '''Converts a given input to a coordinate tuple (e.g. B5 -> (4, 1))'''
    # Split input into 2 parts
    try:
        column = input[0].upper()
        row = int(input[1]) - 1

        # Convert letter into number by subtracting ASCII code
        column = ord(column) - 65

        # Assert coords are in range
        assert(0  <= column <= 8)
        assert(0 <= row <= 8)

        # Return coordinates
        return (row, column)

    # Error occurred along the way, return (-1, -1)
    except:
        return (-1, -1)


def is_valid_choice(board: list[list[int]], coord: tuple[int, int], input: str) -> bool:
    '''Validates user input. Returns true if valid; false if not.'''
    # Try converting input to int
    try:
        num = int(input)
    except:
        return False
    return True

def get_board_string(board: list[list[int]]) -> str:
    '''Returns the board in a printable format.'''
    # First line
    board_string = "   A B C D E F G H I"

    # Loop through board
    for row in range(9):
        board_string += f"\n{row+1}  "
        for col in range(9):
            board_string += f"{board[row][col]}" if board[row][col] != 0 else " "
            # Add separator
            board_string += "|" if (col == 2 or col == 5) else " "
        # Add separator
        board_string += "\n   -----+-----+-----" if (row == 2 or row == 5) else ""

    return board_string

def main():
    # Game loading
    board = None
    filename = "" # Keep this for save game use
    while board is None:
        filename = input("Enter the json file to load (excluding extension): ")
        board = load_game(filename)

    # First time display
    print(get_board_string(board))
    print("Specify a coordinate to edit or 'Q' to save and quit")

    # Game loop
    done = False
    while not done:
        # Get user cell choice
        valid_coord = False
        while not valid_coord:
            choice = input("> ")

            # User quit
            if choice.upper() == "Q":
                today = datetime.datetime.today()
                save_index = filename.find(".save")
                # Slice off save string if it exists
                if save_index != -1:
                    filename = filename[:save_index]
                save_name = filename + f".save{today.month:02}{today.day:02}{today.hour:02}{today.minute:02}" + ".json"
                save_game(save_name, board)
                done = True
                valid_coord = True

            # User didn't quit
            else:
                coord = convert_to_coordinate(choice)

                # See if coord was invalid
                if coord[0] == -1 and coord[1] == -1:
                    print(f"Error: {choice} is invalid.")

                # See if coord is already full
                elif board[coord[0]][coord[1]] != 0:
                    print(f"Error: {choice} is already filled.")
                    print(f"Coord: ({coord[0]},{coord[1]}), value: {board[coord[0]][coord[1]]}")

                # Valid otherwise
                else:
                    valid_coord = True

        # Only if user didn't quit
        if not done:
            # Get user number input
            num = input(f"What number goes in {choice}? ")
            while not is_valid_choice(board, coord, num):
                print(f"{num} is invalid. Try a different number.")
                num = input(f"What number goes in {choice}? ")

            board[coord[0]][coord[1]] = num

            # Display board
            print(get_board_string(board))


if __name__ == "__main__":
    main()
