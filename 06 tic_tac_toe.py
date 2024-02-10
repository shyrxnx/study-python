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

board_arranged = [[board['Top-L'], board['Top-M'], board['Top-R']],
                  [board['Mid-L'], board['Mid-M'], board['Mid-R']],
                  [board['Bot-L'], board['Bot-M'], board['Bot-R']]]

character = input("Enter character to use: ")

while True:
    choice = input("Enter choice ( Top, Mid, Bot and - and L, M, R): ")
    if choice in board:
        board[choice] = character
        print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
        print("-----")
        print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
        print("-----")
        print(board['Bot-L'] + '|' + board['Bot-M'] + '|' + board['Bot-R'])
        print("\n")
    else:
        print("Invalid choice. Please try again.")
