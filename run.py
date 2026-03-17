import random
import os
import json
from colorama import Fore, init

init(autoreset=True)

# ------------------ UI ------------------

def display_logo():
    print(Fore.GREEN + r"""
 ____        _   _   _           _     _       
|  _ \      | | | | | |         | |   (_)      
| |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  
|  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                       | |    
                                       |_|    
""")


def welcome():
    print(Fore.GREEN + "Welcome to Battleship CLI!\n")
    print("Try to sink the hidden ship.")
    print("You have 5 turns.\n")


# ------------------ BOARD ------------------

def create_board():
    return [["~"] * 5 for _ in range(5)]


def print_board(board):
    print("\n   0 1 2 3 4")
    print("  -----------")
    for i, row in enumerate(board):
        print(f"{i} | {' '.join(row)}")


# ------------------ GAME LOGIC ------------------

def place_ship():
    return (random.randint(0, 4), random.randint(0, 4))


def get_guess():
    if os.getenv("PORT"):  # Heroku mode
        return (random.randint(0, 4), random.randint(0, 4))

    try:
        row = int(input("Row (0-4): "))
        col = int(input("Col (0-4): "))
        return (row, col)
    except:
        print("Invalid input")
        return None


# ------------------ DATA ------------------

def save_score(result):
    data = {"result": result}

    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except:
        scores = []

    scores.append(data)

    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)


# ------------------ GAME ------------------

def play_game():
    display_logo()
    welcome()

    board = create_board()
    ship = place_ship()
    guesses = []

    for turn in range(5):
        print(f"Turn {turn + 1}/5")
        print_board(board)

        guess = get_guess()

        if guess is None:
            continue

        if guess in guesses:
            print("You already guessed that spot!\n")
            continue

        guesses.append(guess)

        row, col = guess

        if guess == ship:
            board[row][col] = "S"
            print("\n🎯 You sunk the ship!")
            print_board(board)
            save_score("Win")
            return
        else:
            print("❌ Miss!\n")
            board[row][col] = "X"

    print("\nGame Over!")
    print(f"The ship was at {ship}")
    save_score("Loss")


# ------------------ RUN ------------------

if __name__ == "__main__":
    play_game()