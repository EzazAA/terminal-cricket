import random
import time
from colorama import init, Fore, Style
import sys
import os
from boundary import clear_terminal, print_boundary
from loading import loading_animation
from animation import game_over_screen, goodbye_screen, show_bat, show_ball

# Initialize Colorama
init(autoreset=True)

def generate_computer_choice():
    """Generate a random choice for the computer (1 to 6)."""
    return random.randint(1, 6)

def get_user_choice():
    """Prompt the user to choose a number between 1 and 6, or quit by entering 'q'."""
    while True:
        choice = input(Fore.GREEN + "Choose any number between 1 and 6 (or 'q' to quit): " + Style.RESET_ALL)
        if choice.lower() == 'q':
            goodbye_screen()
            sys.exit()  # Exit the game
        try:
            choice = int(choice)
            if 1 <= choice <= 6:
                return choice
            else:
                print("Choose a valid number.")
        except ValueError:
            print("Enter a valid number or 'q' to quit.")


def perform_user_batting():
    """Handle the user's batting turn, updating their score."""
    global runs_user
    print("=============================================================\nNow your batting")
    for _ in range(6):
        user_input = get_user_choice()
        computer_input = generate_computer_choice()
        print(f"You batted for {user_input} and computer bowled {computer_input}")
        time.sleep(0.5)
        
        if user_input == computer_input:
            print(Fore.RED + "You are out!\n=============================================================" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + f"You got {user_input} runs" + Style.RESET_ALL)
            runs_user += user_input
            print(Fore.YELLOW + f"Your current score: {runs_user}" + Style.RESET_ALL)
            time.sleep(0.5)

def perform_user_bowling():
    """Handle the user's bowling turn, updating the CPU's score."""
    global runs_cpu
    print("=============================================================\nNow your bowling")
    for _ in range(6):
        user_input = get_user_choice()
        computer_input = generate_computer_choice()
        print(f"You bowled for {user_input} and computer batted {computer_input}")
        time.sleep(0.5)

        if user_input == computer_input:
            print(Fore.RED + "CPU is out!\n=============================================================" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + f"CPU got {computer_input} runs" + Style.RESET_ALL)
            runs_cpu += computer_input
            print(Fore.YELLOW + f"CPU's current score: {runs_cpu}" + Style.RESET_ALL)
            time.sleep(0.5)

def determine_winner():
    """Compare scores and announce the winner."""
    print(f"Final Score - You: {runs_user}, CPU: {runs_cpu}")
    if runs_cpu > runs_user:
        print(Fore.BLUE + '--CPU WON--' + Style.RESET_ALL)
    elif runs_cpu < runs_user:
        print(Fore.BLUE + '--YOU WON--' + Style.RESET_ALL)
    else:
        print(Fore.BLUE + '--IT\'S A DRAW--' + Style.RESET_ALL)

def decide_toss():
    """Prompt the user to choose batting or bowling, or quit by entering 'q'."""
    while True:
        choice = input(Fore.GREEN + "Choose batting(1) or bowling(2) (or 'q' to quit): " + Style.RESET_ALL)
        if choice.lower() == 'q':
            goodbye_screen()
            sys.exit()  # Exit the game
        try:
            choice = int(choice)
            if choice == 1:
                show_bat()  # Display the bat ASCII art when batting is chosen
                return choice
            elif choice == 2:
                show_ball()  # Display the ball ASCII art when bowling is chosen
                return choice
            else:
                print("Choose a valid option (1 or 2).")
        except ValueError:
            print("Enter a valid number or 'q' to quit.")

# Global score variables
runs_user = 0
runs_cpu = 0

# Determine who bats or bowls first
toss_output = decide_toss()

def play_game():

    clear_terminal()
    print_boundary()
    loading_animation()

    toss_output = decide_toss()  # Show ASCII art after toss decision

    """Main function to execute the game flow."""
    if toss_output == 1:
        perform_user_batting()
        perform_user_bowling()
    else:
        perform_user_bowling()
        perform_user_batting()
    determine_winner()
    game_over_screen()

# Start the game
play_game()
