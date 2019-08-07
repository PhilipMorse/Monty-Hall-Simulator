import random
import os

def initializeFile():
    with open("data.txt", "w") as f:
        f.write("Switch\n"
                "Wins\n"
                "0\n"
                "Loses\n"
                "0\n"
                "NoSwitch\n"
                "Wins\n"
                "0\n"
                "Loses\n"
                "0\n")


def pick():
    choice = input("Pick a door (1-3)\n")
    while True:
        if choice == "1" or choice == "2" or choice == "3":
            return int(choice)
        else:
            choice = input("Please enter 1, 2 or 3\n")


def reveal(choice, winner):
    options = [1, 2, 3]
    if winner != choice:
        options.remove(winner)
        options.remove(choice)
    else:
        options.remove(winner)
    return random.choice(options)


def askSwitch(revealed,choice):
    options = [1, 2, 3]
    if revealed != choice:
        options.remove(revealed)
        options.remove(choice)
    else:
        options.remove(revealed)
    answer = input("Would you like to switch to door " + str(options[0]) + "? (y/n)\n")
    while True:
        if answer == "y":
            return options[0]
        elif answer == "n":
            return choice
        else:
            answer = input("Please enter a valid answer. Would you like to switch doors? (y/n)\n")


def writedata(data):
    numlines = sum(1 for line in open("data.txt", "r"))
    if numlines != 10:
        initializeFile()
    with open("data.txt", "r") as f:
        file_data = f.readlines()
    if data[0] == "Switch":
        if data[1] == "Win":
            file_data[2] = str(int(file_data[2])+1)+"\n"
            print("You win!")
        elif data[1] == "Lose":
            file_data[4] = str(int(file_data[4])+1)+"\n"
            print("You lose!")
        print("Switching has a record of " + file_data[2] + "/" + str(int(file_data[2])+int(file_data[4])))
    if data[0] == "NoSwitch":
        if data[1] == "Win":
            file_data[7] = str(int(file_data[7])+1)+"\n"
            print("You win!")
        if data[1] == "Lose":
            file_data[9] = str(int(file_data[9])+1)+"\n"
            print("You lose!")
        print("Not switching has a record of " + file_data[7] + "/" + str(int(file_data[9])+int(file_data[7])))

    with open("data.txt", "w") as f:
        f.writelines(file_data)

while True:
    winner = random.randrange(1, 4)
    choice = pick()
    revealed = reveal(choice, winner)
    print("Door number " + str(revealed) + " does not contain a prize")
    choicefinal = askSwitch(revealed, choice)
    result = []
    result.clear()
    if choicefinal == winner:
        if choice == choicefinal:
            result.append("NoSwitch")
        else:
            result.append("Switch")
        result.append("Win")
    else:
        if choice == choicefinal:
            result.append("NoSwitch")
        else:
            result.append("Switch")
        result.append("Lose")
    writedata(result)
    keep = input("Keep playing? (y/n)")
    if keep!="y":
        break




