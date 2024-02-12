# orig = {
#     'top-l': 0,
#     'top-c': 1,
#     'top-r': 2,
#     'mid-l': 3,
#     'mid-c': 4,
#     'mid-r': 5,
#     'bot-l': 6,
#     'bot-c': 7,
#     'bot-r': 8,
# }
#
# board = [[orig['top-l'], orig['top-c'], orig['top-r']],
#          [orig['mid-l'], orig['mid-c'], orig['mid-r']],
#          [orig['bot-l'], orig['bot-c'], orig['bot-r']]]
#
# print(len(board))
# print(board[1][1])
#
# print("=============")
# print(f"| {orig['top-l']} | {orig['top-c']} | {orig['top-r']} |")
# print("====+===+====")
# print(f"| {orig['mid-l']} | {orig['mid-c']} | {orig['mid-r']} |")
# print("====+===+====")
# print(f"| {orig['bot-l']} | {orig['bot-c']} | {orig['bot-r']} |")
# print("=============")
#
# # This is for the better board
#
#
# #############################################################################################
#
# count = 0
#
# while count < 3:
#     if count % 2 == 0:
#         turn = input("It's you turn player 1: ")
#         count += 1
#     elif count % 2 != 0:
#         turn = input("It's you turn player 2: ")
#         count += 1
#
# # This is for taking turns logic
#
# #############################################################################################
#
#
# orig = {
#     'top-l': "LOL",
#     'top-c': " ",
#     'top-r': " ",
#     'mid-l': " ",
#     'mid-c': "LOL",
#     'mid-r': " ",
#     'bot-l': " ",
#     'bot-c': " ",
#     'bot-r': "LOL",
# }
#
#
# def check_winner(board):
#     if board['top-l'] == board['top-c'] == board['top-r'] == "LOL":
#         print("You won!")
#     elif board['mid-l'] == board['mid-c'] == board['mid-r'] == "LOL":
#         print("You won!")
#     elif board['bot-l'] == board['bot-c'] == board['bot-r'] == "LOL":
#         print("You won!")
#     elif board['top-l'] == board['mid-l'] == board['bot-l'] == "LOL":
#         print("You won!")
#     elif board['top-c'] == board['mid-c'] == board['bot-c'] == "LOL":
#         print("You won!")
#     elif board['top-r'] == board['mid-r'] == board['bot-r'] == "LOL":
#         print("You won!")
#     elif board['top-l'] == board['mid-c'] == board['bot-r'] == "LOL":
#         print("You won!")
#     elif board['top-r'] == board['mid-c'] == board['bot-l'] == "LOL":
#         print("You won!")
#     else:
#         print("The boards are all filled. It's a tie!")
#
#
# check_winner(orig)
#
# # This is for the winner logic
