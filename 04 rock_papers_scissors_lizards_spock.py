import random

computer = random.randint(0, 5)

Rock = 0
Paper = 1
Scissor = 2
Lizard = 3
Spock = 4

playerChoice = (int(input("Choose:\n0 - Rock\n1 - Paper\n2 - Scissor\n3 - Lizard\n4 - Spock\nEnter your choice: ")))

if computer == 0 and playerChoice == 0:
    print("It's a tie!")
elif computer == 0 and playerChoice == 1:
    print("You won!")
elif computer == 0 and playerChoice == 2:
    print("Computer won!")
elif computer == 0 and playerChoice == 3:
    print("Computer won!")
elif computer == 0 and playerChoice == 4:
    print("You won!")

if computer == 1 and playerChoice == 0:
    print("Computer won!")
elif computer == 1 and playerChoice == 1:
    print("It's a tie!")
elif computer == 1 and playerChoice == 2:
    print("You won!")
elif computer == 1 and playerChoice == 3:
    print("You won!")
elif computer == 1 and playerChoice == 4:
    print("Computer won!")

if computer == 2 and playerChoice == 0:
    print("You won!")
elif computer == 2 and playerChoice == 1:
    print("Computer won!")
elif computer == 2 and playerChoice == 2:
    print("It's a tie!")
elif computer == 2 and playerChoice == 3:
    print("Computer won!")
elif computer == 2 and playerChoice == 4:
    print("You won!")

if computer == 3 and playerChoice == 0:
    print("You won!")
elif computer == 3 and playerChoice == 1:
    print("Computer won!")
elif computer == 3 and playerChoice == 2:
    print("You won!")
elif computer == 3 and playerChoice == 3:
    print("It's a tie!")
elif computer == 3 and playerChoice == 4:
    print("Computer won!")

if computer == 4 and playerChoice == 0:
    print("Computer won!")
elif computer == 4 and playerChoice == 1:
    print("You won!")
elif computer == 4 and playerChoice == 2:
    print("Computer won!")
elif computer == 4 and playerChoice == 3:
    print("You won!")
elif computer == 4 and playerChoice == 4:
    print("It's a tie!")

print(f"The computer picked {computer} and you picked {playerChoice}.")
