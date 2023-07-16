import platform, os, random, time

# game variables
MIN = 1
MAX = 10
REWARD = 10

# player variables
CREDITS = 10
PLAYER_NAME = None


def main():
    # clear screen
    clear_screen()

    # print game intro
    intro()

    # get player name
    get_player_name()

    time.sleep(3)
    
    # todo start game loop
    game_loop()


def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def intro():
    print("-"*50, "MAGIC NUMBER GAME", "-"*50)
    print(f"I have a number between {MIN} and {MAX}. Can you guess it?")

def get_player_name():
    global PLAYER_NAME
    PLAYER_NAME = input("What is your name?")

def game_loop():
    pass

# start program
main()