# Define the initial board state
board = {
    'Top-L': " ",
    'Top-M': " ",
    'Top-R': " ",
    'Mid-L': " ",
    'Mid-M': " ",
    'Mid-R': " ",
    'Bot-L': " ",
    'Bot-M': " ",
    'Bot-R': " "
}

# Function to print the board
def print_board(board):
    print(f"| {board['Top-L']} | {board['Top-M']} | {board['Top-R']} |")
    print("====+===+====")
    print(f"| {board['Mid-L']} | {board['Mid-M']} | {board['Mid-R']} |")
    print("====+===+====")
    print(f"| {board['Bot-L']} | {board['Bot-M']} | {board['Bot-R']} |")


def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in ['Top', 'Mid', 'Bot']:
        if board[f'{row}-L'] == board[f'{row}-M'] == board[f'{row}-R'] != " ":
            return True
    for col in ['L', 'M', 'R']:
        if board[f'Top-{col}'] == board[f'Mid-{col}'] == board[f'Bot-{col}'] != " ":
            return True
    if board['Top-L'] == board['Mid-M'] == board['Bot-R'] != " ":
        return True
    if board['Top-R'] == board['Mid-M'] == board['Bot-L'] != " ":
        return True
    return False


def is_board_full(board):
    return " " not in board.values()


# Function to get player's character choice (X or O)
def char_use():
    while True:
        character_1 = input(
            "Pick your character (X or O): ").upper()  # Convert input to uppercase for case-insensitivity
        if character_1 == 'X' or character_1 == 'O':
            character_2 = 'O' if character_1 == 'X' else 'X'  # Set the second player's character opposite to the first player's
            break
        else:
            print("Invalid input! Choose only from X or O")
    return character_1, character_2


# Get characters for players
character_1, character_2 = char_use()

# Game loop
while True:
    # Player's choice input
    choice = input("Enter choice (Top, Mid, Bot and - and L, M, R): ").title()  # Capitalize the input for consistency
    if choice in board and board[choice] == " ":  # Check if the choice is valid and the cell is empty
        board[choice] = character_1  # Set the player's character to the chosen cell
    else:
        print("Invalid choice or cell already occupied. Please try again.")
        continue

    # Print the updated board
    print_board(board)

    # Check for a win or draw condition
    if check_winner(board):
        print(f"Congratulations! {character_1} wins!")
        break  # End the game if there's a winner

    if is_board_full(board):
        print("It's a tie!")
        break  # End the game if the board is full and there's no winner

    # Swap characters for the next player's turn
    character_1, character_2 = character_2, character_1
