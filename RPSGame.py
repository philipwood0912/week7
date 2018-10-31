from random import randint
pchealth = 3
myhealth = 3
z = 0
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]

player = False



# make the computer pick one item at random
computer = choices[randint(0, 2)]


while player is False:
    print("")
    print("=======================")
    print("| Choose your weapon! |")
    print("=======================")
    print("Your Health: " + str(myhealth))
    print("Computers Health: " + str(pchealth))


    player = input("Rock, Paper, Scissors?\n")
    print("Player chooses:", player)

    if (player == computer):
        print("Computer chooses:", computer)
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer chooses:", computer)
            print("You lose the round,", computer, "covers", player)
            myhealth = myhealth - 1
        else:
            print("Computer chooses:", computer)
            print("You win the round,", player, "smashes", computer)
            pchealth = pchealth - 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Computer chooses:", computer)
            print("You lose the round,", computer, "cuts", player)
            myhealth = myhealth - 1

        else:
            print("Computer chooses:", computer)
            print("You win the round,", player, "covers", computer)
            pchealth = pchealth - 1

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer chooses:", computer)
            print("You lose the round,", computer, "smashes", player)
            myhealth = myhealth - 1

        else:
            print("Computer chooses:", computer)
            print("You win the round,", player, "cuts", computer)
            pchealth = pchealth - 1

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    player = False
    computer = choices[randint(0, 2)]

    if pchealth is z:
        print(" ______________")
        print("|              |")
        print("|   You Win !  |")
        print("|______________|")
        print("")
        player = input("Would you like to play again? y / n\n")
        pchealth = pchealth + 3
        myhealth = pchealth
        if player == "y":
            player = False
        if player == "n":
            break

    if myhealth is z:
        print(" ______________")
        print("|              |")
        print("|   You Lose   |")
        print("|______________|")
        print("")
        player = input("Would you like to play again? y / n\n")
        myhealth = myhealth + 3
        pchealth = myhealth
        if player == "y":
            player = False
        if player == "n":
            break
