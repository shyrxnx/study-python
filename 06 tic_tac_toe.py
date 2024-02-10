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


def char_use():
    while True:
        character_1 = input("Pick your character (X or O): ")
        if character_1 == 'X':
            character_2 = 'O'
            break
        elif character_1 == 'O':
            character_2 = 'X'
            break
        else:
            print("Invalid input! Choose only from X or O")
    return character_1, character_2


character_1, character_2 = char_use()

while True:
    choice = input("Enter choice (Top, Mid, Bot and - and L, M, R): ")
    if choice in board:
        if board[choice] == " ":
            board[choice] = character_1
        else:
            print("Cell already occupied. Please try again.")
            continue

        print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
        print("-----")
        print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
        print("-----")
        print(board['Bot-L'] + '|' + board['Bot-M'] + '|' + board['Bot-R'])
        print("\n")

        # Swap characters for the next player's turn
        character_1, character_2 = character_2, character_1
    else:
        print("Invalid choice. Please try again.")
