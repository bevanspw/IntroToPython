import random

def choice_to_text(c):
    if c == 1:
        return "Rock"
    elif c == 2:
        return "Paper"
    else:
        return "Scissors"


while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice:"))
    choice_text = choice_to_text(choice)

    computer_choice = random.randint(1, 3)
    computer_choice_text = choice_to_text(computer_choice)

    print(choice_text, 'Vs', computer_choice_text)

    if choice == computer_choice:
        print("Draw!!")
    else:
        # User picks paper beats rocks
        if choice == 2 and computer_choice == 1:
            print("User wins!")
        # User picks scissors beats paper
        elif choice == 3 and computer_choice == 2:
            print("User wins!")
        # User picks rocks beats scissors
        elif choice == 1 and computer_choice == 3:
            print("User wins!")
        else:
            print("Computer wins!")

    quit = input("Do you wish to continue y/n:")
    if quit.lower() == "n":
        break
