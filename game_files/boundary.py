import os

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_boundary():
    """Print a simple boundary around the game screen."""
    print("#" * 40)
    print("#" + " " * 38 + "#")
    print("#" + " WELCOME TO TERMINAL CRICKET " + "#")
    print("#" + " " * 38 + "#")
    print("#" * 40)