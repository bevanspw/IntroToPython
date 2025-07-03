import random

secret_number = random.randint(1, 100)

guess = int(input("Guess a number between 1-100:"))

while guess != secret_number:
    if guess < secret_number:
        print("sorry, number is too low")
    else:
        print("sorry, number is too high")

    guess = int(input("Guess a number between 1-100:"))

print("Good Guess!!")