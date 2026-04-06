import random
import json
from colorama import Fore, init

init(autoreset=True)

# ------------------ INPUT ------------------

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
    width = 70

    print(Fore.GREEN + "=" * width)
    print("🍽️  BATTLESHIP COMMAND CENTER  🍽️".center(width))
    print("=" * width)

    print("\n" + "🎯 Mission Brief".center(width))
    print("-" * width)

    print("Sink all hidden enemy ships before you run out of turns.".center(width))
    print("Enter coordinates to attack (row and column).".center(width))
    print("Good luck, commander!\n".center(width))

def get_player_name():
    while True:
        name = get_input("👉 Enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")

# ------------------ GAME LOGIC ------------------

def create_board(size=5):
    return [["~" for _ in range(size)] for _ in range(size)]

def print_board(board):
    print("\n" + "   0 1 2 3 4".center(50))
    print("  ----------".center(50))

    for i, row in enumerate(board):
        print(f"{i} | " + " ".join(row).center(30))

def place_ships(board, num_ships=2):
    size = len(board)
    ships = []

    while len(ships) < num_ships:
        ship = (random.randint(0, size - 1), random.randint(0, size - 1))
        if ship not in ships:
            ships.append(ship)

    return ships

def get_guess(size):
    while True:
        try:
            row = int(get_input("Row (0-4): "))
            col = int(get_input("Col (0-4): "))

            if 0 <= row < size and 0 <= col < size:
                return (row, col)
            else:
                print(Fore.RED + "Out of bounds!")

        except ValueError:
            print(Fore.RED + "Enter numbers only!")

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

# ------------------ GAME ------------------

def play_game():
    display_logo()
    welcome()

    player = get_player_name()
    print(Fore.GREEN + f"\nGood luck, {player}!\n".center(70))

    board = create_board()
    ships = place_ships(board, 2)

    turns = 5
    guesses = []
    hits = 0

    while turns > 0:
        print(Fore.YELLOW + f"\n⚔️  Turn {6 - turns}/5 ⚔️\n".center(70))
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
            print(Fore.GREEN + "🎯 DIRECT HIT!".center(70))

            if hits == len(ships):
                print(Fore.GREEN + "\n🚢 You sunk all ships!")
                print_board(board)
                save_score(player, "Win")
                return
        else:
            print(Fore.RED + "❌ Target missed!".center(70))
            board[row][col] = "X"

        turns -= 1
        print(f"Turns left: {turns}")

    print(Fore.RED + f"\nGame Over! Ships were at {ships}")
    save_score(player, "Loss")

# ------------------ RUN ------------------

if __name__ == "__main__":
    play_game()