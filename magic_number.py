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

    # todo get player name
    # todo start game loop

def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def intro():
    print("-"*50, "MAGIC NUMBER GAME", "-"*50)
    print(f"I have a number between {MIN} and {MAX}. Can you guess it?")

def get_player_name() -> str:
    pass


# start program
main()