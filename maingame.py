class GameChoice:
    game1="1"
    game2="2"
    game3="3"

def home():
    choices=GameChoice()
    usrname=input("Enter your username: ")
    age=int(input("Enter your age: "))
    if (age>6):
        if (type(usrname)==str and type(age)==int):
            print("Hello " + usrname + ", Welcome to the Mind Reader")

            print("Here are the list of the games available: ")
            print("1. All you get is Simple")
            print("2. Divide and Rule")
            print("3. You're Lucky")
            usrchoice=input("What game would you like to play? (enter the number only!) ")
            if (usrchoice==choices.game1):
                return game1()
            if (usrchoice==choices.game2):
                return game2()
            if (usrchoice==choices.game3):
                return game3()
            else:
                print("This game doesn't exist!")
    else:
        print("You're under-aged to play this game")
    
    

    


def game1():
    print("ABC")
def game2():
    print("DEF")
def game3():
    print("GHI")
    

home()