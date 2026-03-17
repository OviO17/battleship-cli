import random

def create_board():
    return [["~"] * 5 for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship():
    return (random.randint(0, 4), random.randint(0, 4))

def play_game():
    board = create_board()
    ship = place_ship()

    print("Welcome to Battleship!")
    print_board(board)

    for turn in range(5):
        try:
            row = int(input("Row (0-4): "))
            col = int(input("Col (0-4): "))
        except:
            print("Invalid input")
            continue

        if (row, col) == ship:
            print("You sunk the ship!")
            return
        else:
            print("Miss!")

    print("Game Over!")

if __name__ == "__main__":
    play_game()