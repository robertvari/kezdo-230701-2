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
    clear_screen()

    magic_number = random.randint(MIN, MAX)
    max_tries = 3
    print(f"You can try {max_tries} times.")

    player_guess = input("Your guess?")
    while player_guess != str(magic_number):
        clear_screen()
        
        max_tries -= 1
        if max_tries == 0:
            break

        print(f"Wrong guess. You have {max_tries} tries. Try Again.")
        player_guess = input("Your guess?")

    clear_screen()

    # check final result
    check_results(magic_number, player_guess)

    # ask player for next round
    ask_to_restart_game()

def check_results(magic_number, player_guess):
    global CREDITS

    if player_guess == str(magic_number):
        print(f"You win {REWARD} credits {PLAYER_NAME}!!!")
        CREDITS += REWARD
        print("Well done!")
    else:
        print(f"My number was {magic_number}.")
        print(f"You lost {REWARD} credits.")
        CREDITS -= REWARD
    
    print(f"Now you have {CREDITS} credits.")

def ask_to_restart_game():
    if CREDITS <= 0:
        print("You lost all your credits :(")
        print("Game Over")
        exit()
    else:
        player_response = input("Do you want to try again? (y/n)")
        if player_response == "y":
            game_loop()
        else:
            print("Maybe next time :)")
            exit()

# start program
main()