import random
import json
import os
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
    print("Try to sink the hidden ships.")
    print("Good luck!\n")


def get_player_name():
    if os.getenv("PORT"):
        return "HerokuUser"

    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


# ------------------ GAME LOGIC ------------------

def create_board(size=5):
    return [["~" for _ in range(size)] for _ in range(size)]


def print_board(board):
    print("\n   " + " ".join(str(i) for i in range(len(board))))
    print("  " + "--" * len(board))

    for i, row in enumerate(board):
        print(f"{i} |" + " ".join(row))


def place_ships(board, num_ships=2):
    size = len(board)
    ships = []

    while len(ships) < num_ships:
        ship = (random.randint(0, size - 1), random.randint(0, size - 1))
        if ship not in ships:
            ships.append(ship)

    return ships


def get_guess(size):
    if os.getenv("PORT"):
        return (random.randint(0, size - 1), random.randint(0, size - 1))

    while True:
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter col (0-4): "))

            if 0 <= row < size and 0 <= col < size:
                return (row, col)
            else:
                print("Out of bounds!")

        except ValueError:
            print("Enter numbers only!")


# ------------------ DATA ------------------

def save_score(player, result):
    data = {
        "player": player,
        "result": result
    }

    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
    except:
        scores = []

    scores.append(data)

    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)


def choose_difficulty():
    if os.getenv("PORT"):
        return 5  # default for Heroku

    print("\nSelect Difficulty:")
    print("1. Easy (5 turns)")
    print("2. Medium (4 turns)")
    print("3. Hard (3 turns)")

    while True:
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            return 5
        elif choice == "2":
            return 4
        elif choice == "3":
            return 3
        else:
            print("Invalid choice!")


# ------------------ GAME ------------------

def play_game():
    display_logo()
    welcome()
    player = get_player_name()

    print(f"\nGood luck, {player}!\n")

    board = create_board()
    ships = place_ships(board, 2)
    turns = choose_difficulty()

    guesses = []
    hits = 0

    while turns > 0:
        print_board(board)
        guess = get_guess(len(board))

        if guess in guesses:
            print(Fore.YELLOW + "You already guessed that spot!")
            continue

        guesses.append(guess)
        row, col = guess

        if guess in ships:
            board[row][col] = "S"
            hits += 1
            print(Fore.GREEN + "🎯 Hit!")

            if hits == len(ships):
                print(Fore.GREEN + "🚢 You sunk all ships!")
                print_board(board)
                save_score(player, "Win")
                return
        else:
            print(Fore.RED + "Miss!")
            board[row][col] = "X"

        turns -= 1
        print(f"Turns left: {turns}")

    print(Fore.RED + f"\nGame Over! Ships were at {ships}")
    save_score(player, "Loss")


# ------------------ REPLAY ------------------

def play_again():
    if os.getenv("PORT"):
        return False

    while True:
        choice = input("Play again? (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input!")


# ------------------ RUN ------------------

if __name__ == "__main__":
    while True:
        play_game()
        if not play_again():
            print("Thanks for playing!")
            break