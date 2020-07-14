import random

tries = 10
error = True
start, end = 0, 0
default = input(
    "Choose the range of the random numbers separated by comma e.g(start,end)\nYou can Hit Enter to use the default settings. ")


def Less_or_Greater_or_Win(inp):
    global tries
    if inp < number:
        tries -= 1
        if number-inp > 10:
            print("You are way toooo low, the number is greater than "+str(inp))
        else:
            print("Almost there, the number is greater than "+str(inp))
        return 'less'
    elif inp > number:
        tries -= 1
        if inp - number > 10:
            print("You are way toooo high, the number is less than "+str(inp))
        else:
            print("Almost there, the number is less than "+str(inp))
        return 'greater'
    else:
        tries -= 1
        many = 10-tries
        many = str(many)+' tries' if many > 1 else str(many)+' try'
        print("You WIN! the secret number is "+str(inp)+"\nYou won with just "+many
              )
        return 'win'


while error:
    if len(default) == 0:
        start, end = 1, 101
        number = random.randint(start, end)
        error = False
    else:
        try:
            start, end = map(int, default.split(','))
            number = random.randint(start, end)
            error = False
        except:
            print("There's an error with your input, remember to seprate value with comma i.e \'1,100\' or simply hit the ENTER key on your keyboard")
            default = input("Try Again ")

print('The Number can be any number from '+str(start)+" to "+str(end-1))
choice = input("Guess the Number: ")
while tries > 0:
    result = Less_or_Greater_or_Win(int(choice))
    playAgain = ''
    if result == 'less' or result == 'greater':
        print("You have "+str(tries)+" left.")
        choice = input("Try Again: ")
    else:
        while playAgain != 'Y' and playAgain != 'N':
            playAgain = input(
                "Do you want to play again? y for YES, n for NO: ").upper()
            if playAgain == 'Y':
                break
            elif playAgain == 'N':
                print("Thanks for playing!")
                exit()
            else:
                print("Wrong Input, Try Again.\n")
