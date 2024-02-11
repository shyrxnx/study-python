# orig =  {
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

# board = [[orig['top-l'], orig['top-c'], orig['top-r']],
#          [orig['mid-l'], orig['mid-c'], orig['mid-r']],
#          [orig['bot-l'], orig['bot-c'], orig['bot-r']]]

# print(len(board))
# print(board[1][1])


# print("=============")
# print(f"| {orig['top-l']} | {orig['top-c']} | {orig['top-r']} |")
# print("====+===+====")
# print(f"| {orig['mid-l']} | {orig['mid-c']} | {orig['mid-r']} |")
# print("====+===+====")
# print(f"| {orig['bot-l']} | {orig['bot-c']} | {orig['bot-r']} |")
# print("=============")


# # This is for the better board


# #############################################################################################

# count = 0

# while count < 3:
#     if count % 2 == 0:
#         turn = input("It's you turn player 1: ")
#         count += 1
#     elif count % 2 != 0:
#         turn = input("It's you turn player 2: ")
#         count += 1

# # This is for taking turns logic

# #############################################################################################


orig = {
    'top-l': "LOL",
    'top-c': " ",
    'top-r': " ",
    'mid-l': " ",
    'mid-c': "LOL",
    'mid-r': " ",
    'bot-l': " ",
    'bot-c': " ",
    'bot-r': "LOL",
}

if orig['top-l'] == orig['top-c'] == orig['top-r'] == "LOL":
    print("You won!")
elif orig['mid-l'] == orig['mid-c'] == orig['mid-r'] == "LOL":
    print("You won!")
elif orig['bot-l'] == orig['bot-c'] == orig['bot-r'] == "LOL":
    print("You won!")
elif orig['top-l'] == orig['mid-l'] == orig['bot-l'] == "LOL":
    print("You won!")
elif orig['top-c'] == orig['mid-c'] == orig['bot-c'] == "LOL":
    print("You won!")
elif orig['top-r'] == orig['mid-r'] == orig['bot-r'] == "LOL":
    print("You won!")
elif orig['top-l'] == orig['mid-c'] == orig['bot-r'] == "LOL":
    print("You won!")
elif orig['top-r'] == orig['mid-c'] == orig['bot-l'] == "LOL":
    print("You won!")
else:
    print("Something is wrong")
