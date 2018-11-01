from random import randint

pchealth = 3
myhealth = 3
z = 0
# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]

player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# Define a win or lose function
def winorlose(status):
    # handle win or lose with the status we pass in
    print("Called the win or lose function")
    print("===============================")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N:")

    if choice == "y" or choice == "Y":
        global pchealth
        global myhealth
        global player
        global computer

        pchealth = 3
        myhealth = 3
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "n" or choice == "N":
        exit()




while player is False:
    print("")
    print("=======================")
    print("| Choose your weapon! |")
    print("=======================")
    print("Your Health: " + str(myhealth))
    print("Computers Health: " + str(pchealth))


    player = input("Rock, Paper, Scissors?\n")

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

    if myhealth is z:
        winorlose("Lost")

    if pchealth is z:
        winorlose("Win")
