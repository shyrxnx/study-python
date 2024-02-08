import random

name = input("Good day! What is your name?\nEnter name: ")
print(f"Hello {name} it is nice to meet you!")

secretNumber = random.randint(0, 10)

print(f"Well, {name}, I'm thinking of a number between 0 to 10.")

for i in range(0, 5):
    guess = (int(input("Take a guess.\n\nEnter your guess: ")))
    if guess > secretNumber:
        print("Your guess is too high!")
    elif guess < secretNumber:
        print("Your guess is too low!")
    else:
        break

if guess == secretNumber:
    print(f"Good job {name}! You guessed my number in {i + 1} tries.")
else:
    print(f"Too bad you're out of guess. The number I was thinking of is {secretNumber}.")
