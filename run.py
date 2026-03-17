import random
import json
from colorama import Fore, init

init(autoreset=True)

# ------------------ SAFE INPUT ------------------

def get_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return ""

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

# ------------------ GAME LOGIC ------------------

def create_board():
    return [["~"] * 5 for _ in range(5)]

def print_board(board):
    print("\n   0 1 2 3 4")
    print("  ----------")
    for i, row in enumerate(board):
        print(f"{i} | " + " ".join(row))

def place_ship():
    return (random.randint(0, 4), random.randint(0, 4))

def get_guess():
    while True:
        try:
            row = int(get_input("Row (0-4): "))
            col = int(get_input("Col (0-4): "))

            if 0 <= row < 5 and 0 <= col < 5:
                return (row, col)
            else:
                print(Fore.RED + "Out of bounds!")

        except ValueError:
            print(Fore.RED + "Enter numbers only!")

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

    for turn in range(5):
        print(Fore.YELLOW + f"\nTurn {turn + 1}/5")
        print_board(board)

        guess = get_guess()
        row, col = guess

        if guess == ship:
            print(Fore.GREEN + "\n🎯 You sunk the ship!")
            board[row][col] = "S"
            print_board(board)
            save_score("Win")
            return
        else:
            print(Fore.RED + "❌ Miss!")
            board[row][col] = "X"

    print(Fore.RED + f"\nGame Over! Ship was at {ship}")
    save_score("Loss")

# ------------------ RUN ------------------

if __name__ == "__main__":
    play_game()