# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part was figuring out how to use the dump and load
#      functions from json. I had to look up what each function expected; I
#      found sample code which was helpful for implementation. Other than that,
#      the logic was simple to implement.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# For debugging purposes
DEBUG = False

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Try reading the file
    try:
        # Open file for reading
        with open(filename, "r") as f:
            # Get data and load into board
            data = json.load(f)
            board = data["board"]

            # If game was ended by winning, return blank board
            if (game_done(board)):
                return blank_board['board']
            return board
    # No file exists; return blank board
    except FileNotFoundError as e:
        if DEBUG:
            print(f"No save data found called \'{filename}\'.")
        return blank_board['board']
    # File data corrupted or otherwise unexpected; return blank board
    except Exception as e:
        if DEBUG:
            print(f"Save data corrupted. Error: {e}")
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Get current game in json state
    save_data = {
        "board": board
    }

    # Open file with write permissions (overwriting old data)
    try:
        with open(filename, "w") as f:
            # Dump json
            json.dump(save_data, f)
    except Exception as e:
        if DEBUG:
            print(f"Error saving game data: {e}")

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Loop through the current board
    for i in range(len(board)):
        # Board spaces done by modulus; i + 1 % 3
        # 1 = left, 2 = middle, 0 = right
        print(f" {board[i]} ", end="")
        match((i + 1) % 3):
            # Right spot; newline after
            case 0:
                print()
            # Left spot; pipe character
            case 1:
                print("|", end="")
            # Middle spot; pipe character
            case 2:
                print("|", end="")
        # Print separating line after i = 2 and i = 5
        if (i == 2 or i == 5):
            print("---+---+---")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # X goes first
    # Flip whether or not it is X's turn based on every non-blank board space.
    x_turn = True
    for space in board:
        if (space != BLANK):
            x_turn = not x_turn

    return x_turn

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Play the game until game is done or user has decided to quit.
    done = False
    while not done:
        # Get turn
        symbol = X if is_x_turn(board) else O
        # Get user's choice
        choice = input(f"{symbol}> ")

        # User quit
        if choice == 'q':
            done = True

        # User didn't quit
        else:
            # Try parsing choice
            try:
                choice = int(choice) - 1

                # See if choice is a valid space
                if (choice < 0 or choice > 8):
                    print("Error: invalid choice. Please enter valid space (1-9)")

                # See if that space is already taken up
                elif board[choice] != BLANK:
                    print("Error: spot already taken. Please enter a blank spot.")

                # Valid choice, update board
                else:
                    board[choice] = symbol

            # Parse failed
            except:
                print("Error: invalid choice. Please enter a number (1-9)")

            # Display board
            display_board(board)

            # Done if game is over
            done = game_done(board, True)

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# Try getting board state from save data.
board = read_board("ttt_save.json")

# Display board
display_board(board)

# Play game
play_game(board)

# Save data
save_board("ttt_save.json", board)