import random


def guess_the_number():
    secret_number = random.randint(0, 10)

    print(f"\nWell, I'm thinking of a number between 0 to 10.")

    tries = 5

    for i in range(5):
        guess = (int(input(f"Take a guess. You have {tries} guess remaining.\n\nEnter your guess: ")))
        tries -= 1
        if guess > secret_number:
            print("Your guess is too high!")
        elif guess < secret_number:
            print("Your guess is too low!")
        else:
            break

    if guess == secret_number:
        print(f"Good job! You guessed my number in {i + 1} tries.\n")
    else:
        print(f"Too bad you're out of guess. The number I was thinking of is {secret_number}.\n")


def rpsls():
    choices = {
        0: "Rock",
        1: "Paper",
        2: "Scissor",
        3: "Lizard",
        4: "Spock"
    }

    outcomes = {
        0: {0: "It's a tie!", 1: "You won!", 2: "Computer won!", 3: "Computer won!", 4: "You won!"},
        1: {0: "Computer won!", 1: "It's a tie!", 2: "You won!", 3: "You won!", 4: "Computer won!"},
        2: {0: "You won!", 1: "Computer won!", 2: "It's a tie!", 3: "Computer won!", 4: "You won!"},
        3: {0: "You won!", 1: "Computer won!", 2: "You won!", 3: "It's a tie!", 4: "Computer won!"},
        4: {0: "Computer won!", 1: "You won!", 2: "Computer won!", 3: "You won!", 4: "It's a tie!"},
    }

    computer = random.randint(0, 5)
    player_choice = (
        int(input("Choose:\n0 - Rock\n1 - Paper\n2 - Scissor\n3 - Lizard\n4 - Spock\nEnter your choice: ")))
    outcome = outcomes[computer][player_choice]

    print(outcome)
    print(f"The computer picked {choices[computer]} and you picked {choices[player_choice]}\n")


while True:
    choice = (int(input("Choose your game:\n1 - Guess the Number\n2 - RPSLS\n3 - Exit\nEnter choice: ")))
    if choice == 1:
        guess_the_number()
    elif choice == 2:
        rpsls()
    elif choice == 3:
        print("\nExiting the program.....")
        break
