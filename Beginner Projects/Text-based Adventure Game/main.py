
class ForestHunt():
    """
    This is a mini text adventure game I used to learn conditional statements and loops
    Source: https://trinket.io/python/e5a03e7cbc
    Call @intro to get the game started
    """

    def __init__(self):
        self.yes_no = ["yes", "no"]
        self.directions = ["left", "right", "forward", "backward"]
        self.name = ''
        self.response = ''

    def intro(self):
        """This is teh function that Introduces the user into the game"""
        self.name = input("What is your name, adventurer?: ")
        print("Greetings, " + self.name +
              ". Let us go on a quest!\nYou find yourself on the edge of a dark forest.\nCan you find your way through?\n")
        self.start_game()

    def start_game(self):
        while self.response not in self.yes_no:
            self.response = input(
                "Would you like to step into the forest?\nyes/no\n")
            if self.response == "yes":
                print(
                    "You head into the forest. You hear crows cawwing in the distance.\n")
            elif self.response == "no":
                print("You are not ready for this quest. Goodbye, " + self.name + ".")
                exit()
            else:
                print("Sorry, I didn't understand that.\n")
        self.response = ''  # Reset the response variable so as to make use of it in next part
        self.next_part()

    def next_part(self):
        while self.response not in self.directions:
            print("To your left, you see a bear.\nTo your right, there is more forest.\nThere is a rock wall directly in front of you.\nBehind you is the forest exit.\n")
            self.response = input(
                "What direction do you move?\nleft/right/forward/backward\n")
            if self.response == "left":
                print("The bear eats you. Farewell, " + self.name + ".")
                exit()
            elif self.response == "right":
                print(
                    "You head deeper into the forest.\nYou find a treasure, you become wealthy and live happily ever after.\nThanks for playing, it was fun hanging out with you "+self.name+'.')
            elif self.response == "forward":
                print("You cannot scale the wall.\n")
                self.response = ""
            elif self.response == "backward":
                print("You leave the forest. Goodbye, " + self.name + ".")
                quit()
            else:
                print("I didn't understand that.\n")


ForestHunt().intro()
