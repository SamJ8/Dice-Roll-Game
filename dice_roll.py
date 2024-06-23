import random
from colorama import Fore

def roll_dice():
    dice_faces = [
        """
        ---------
        |       |
        |   ●   |
        |       |
        ---------""",

        """
        ---------
        | ●     |
        |       |
        |     ● |
        ---------""",

        """
        ---------
        | ●     |
        |   ●   |
        |     ● |
        ---------""",

        """
        ---------
        | ●   ● |
        |       |
        | ●   ● |
        ---------""",

        """
        ---------
        | ●   ● |
        |   ●   |
        | ●   ● |
        ---------""",

        """
        ---------
        | ●   ● |
        | ●   ● |
        | ●   ● |
        ---------"""
    ]
    roll = random.randint(1, 6)
    print(dice_faces[roll-1])
    return roll

def play_game():
    while True:
        score = 0
        while True:
            input(Fore.YELLOW + "Press Enter to roll the dice...")
            roll = roll_dice()
            print(Fore.GREEN + "\nYou rolled:", roll)
            if roll == 1:
                score = 0
                print(Fore.GREEN + "\nYou rolled a 1. Your score is now 0.")
                break
            else:
                score += roll
                print(Fore.BLUE + "\nYour current score is:", score)
                if score >= 20:
                    print(Fore.MAGENTA + "\nCongratulations! You scored 20 or more. Game Over!")
                    break
        play_again = input(Fore.CYAN + "\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()