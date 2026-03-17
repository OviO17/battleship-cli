import random
import os

# ------------------ BOARD ------------------

def create_board():
    return [["~"] * 5 for _ in range(5)]


def print_board(board):
    for row in board:
        print(" ".join(row))


# ------------------ GAME LOGIC ------------------

def place_ship():
    return (random.randint(0, 4), random.randint(0, 4))


def get_guess():
    # Heroku mode (no input allowed)
    if os.getenv("PORT"):
        return (random.randint(0, 4), random.randint(0, 4))

    # Local mode (user input)
    try:
        row = int(input("Row (0-4): "))
        col = int(input("Col (0-4): "))
        return (row, col)
    except:
        print("Invalid input")
        return None


# ------------------ GAME ------------------
def play_game():
    board = create_board()
    ship = place_ship()
    guesses = []

    print("Welcome to Battleship!\n")

    for turn in range(5):
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
            return
        else:
            print("Miss!\n")
            board[row][col] = "X"

    print("\nGame Over!")
    print(f"The ship was at {ship}")


# ------------------ RUN ------------------

if __name__ == "__main__":
    play_game()