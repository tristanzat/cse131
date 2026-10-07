# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      Display and play a game of Sudoku. Allows saving and loading to/from
#      files respectively.
# 4. What was the hardest part? Be as specific as possible.
#      Generating the tests was the most difficult part because I haven't
#      done it before. The only new code that needed to be implemented was
#      handling either coordinate format and checking if a number was valid.
# 5. How long did it take for you to complete the assignment?
#      45 minutes

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

def convert_to_coordinate(coord: str) -> tuple[int, int]:
    '''Converts a given input to a coordinate tuple (e.g. B5 or 5B -> (4, 1))'''
    # Split input into 2 parts
    try:
        # Trim whitespace
        coord = coord.strip()
        # Assert input is 2 characters
        assert(len(coord) == 2)

        # Separate into number part and letter part
        try:
            row = int(coord[0]) - 1
            column = coord[1].upper()
        except:
            row = int(coord[1]) - 1
            column = coord[0].upper()

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

def get_valid_nums(board: list[list[int]], coord: tuple[int, int]) -> list[int]:
    '''Returns a list of valid numbers for a given square in a sudoku board.'''
    row, col = coord
    valid_nums = []

    for num in range(1, 10):
        failed = False
        # --- Row check ---
        for c in range(9):
            # Check if we fail
            if c != col and board[row][c] == num:
                failed = True
                break

        # Continue checks if we haven't failed
        if not failed:
            # --- Column check ---
            for r in range(9):
                # Check if we fail
                if r != row and board[r][col] == num:
                    failed = True
                    break

            # Continue checks if we haven't failed
            if not failed:
                #--- 3x3 box check ---
                box_row_start = (row // 3) * 3
                box_col_start = (col // 3) * 3

                for r in range(box_row_start, box_row_start + 3):
                    for c in range(box_col_start, box_col_start + 3):
                        if (r, c) != (row, col) and board[r][c] == num:
                            failed = True
                            break

        # Add number to valid list if it never failed
        if not failed:
            valid_nums.append(num)

    return valid_nums

def is_valid_choice(board: list[list[int]], coord: tuple[int, int], num: str) -> bool:
    '''Validates user input. Returns true if valid; false if not.'''

    # --- Input validation ---
    try:
        num = int(num)
    except:
        return False
    if num < 1 or num > 9:
        return False

    # See if it is in the list of valid moves
    if num in get_valid_nums(board, coord):
        return True

    # Number wasn't valid
    return False


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

                # Valid otherwise
                else:
                    valid_coord = True

        # Only if user didn't quit
        if not done:
            valid = False
            exit = False

            while not valid:
                # Get user number input
                num = input(f"Input the number for square {choice}, enter 'h' for a hint, or 'b' to go back to the board > ")
                if num.upper() == "H":
                    print(f"Valid numbers: {get_valid_nums(board, coord)}")

                elif num.upper() == "B":
                    valid = True
                    exit = True
                
                elif not is_valid_choice(board, coord, num):
                    print(f"{num} is invalid. Try a different number.")

                else:
                    valid = True

            # Only do this if we didn't exit to board
            if not exit:
                board[coord[0]][coord[1]] = int(num)

            # Display board
            print(get_board_string(board))


if __name__ == "__main__":
    main()
