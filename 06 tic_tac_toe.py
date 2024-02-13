original = {
    'top-l': " ",
    'top-m': " ",
    'top-r': " ",
    'mid-l': " ",
    'mid-m': " ",
    'mid-r': " ",
    'bot-l': " ",
    'bot-m': " ",
    'bot-r': " "
}


def pretty_board(board):
    print("=============")
    print(f"| {board['top-l']} | {board['top-m']} | {board['top-r']} |")
    print("====+===+====")
    print(f"| {board['mid-l']} | {board['mid-m']} | {board['mid-r']} |")
    print("====+===+====")
    print(f"| {board['bot-l']} | {board['bot-m']} | {board['bot-r']} |")
    print("=============")


def symbol_usage():
    while True:
        symbol = input("Do you want to be X or O?\nEnter choice: ").upper()
        if symbol in ['X', 'O']:
            print(f"Player 1, you are {symbol}.")
            print(f"Player 2, you are {'O' if symbol == 'X' else 'X'}.")
            return symbol, 'O' if symbol == 'X' else 'X'
        else:
            print("Invalid choice of symbol! Choose only from X or O")


def check_for_winner(board, player):
    if board['top-l'] == board['top-m'] == board['top-r'] == player:
        print(f"{player} won! ")
        return True
    elif board['mid-l'] == board['mid-m'] == board['mid-r'] == player:
        print(f"{player} won! ")
        return True
    elif board['bot-l'] == board['bot-m'] == board['bot-r'] == player:
        print(f"{player} won! ")
        return True
    elif board['top-l'] == board['mid-l'] == board['bot-l'] == player:
        print(f"{player} won! ")
        return True
    elif board['top-m'] == board['mid-m'] == board['bot-m'] == player:
        print(f"{player} won! ")
        return True
    elif board['top-r'] == board['mid-r'] == board['bot-r'] == player:
        print(f"{player} won! ")
        return True
    elif board['top-l'] == board['mid-m'] == board['bot-r'] == player:
        print(f"{player} won! ")
        return True
    elif board['top-r'] == board['mid-m'] == board['bot-l'] == player:
        print(f"{player} won! ")
        return True
    elif " " not in board.values():
        print("The boards are all filled. It's a tie!")
        return True
    else:
        return False


pretty_board(original)

symbol_one, symbol_two = symbol_usage()

count = 0
while not check_for_winner(original, symbol_one) and not check_for_winner(original, symbol_two):
    if count % 2 == 0:
        player = "Player 1"
        character = symbol_one
        position = input(f"{player}, choose your position (e.g., top-l, mid-m, etc.): ")
        if position in original and original[position] == " ":
            original[position] = character
            count += 1
            pretty_board(original)
        else:
            print("Invalid choice or cell already occupied. Please try again.")
    elif count % 2 != 0:
        player = "Player 2"
        character = symbol_two
        position = input(f"{player}, choose your position (e.g., top-l, mid-m, etc.): ")
        if position in original and original[position] == " ":
            original[position] = character
            count += 1
            pretty_board(original)
        else:
            print("Invalid choice or cell already occupied. Please try again.")
