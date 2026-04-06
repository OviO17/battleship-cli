# Battleship CLI 🎮

## Introduction

Battleship CLI is a command-line game where the player must locate and sink hidden ships on a 5x5 grid. The game runs in the browser via Heroku using a simulated terminal interface.

The player enters coordinates to attack positions on the board and must sink all ships before running out of turns.

---

## Live Project

👉 [Play the game here](https://battleship-cli-d52472d323d8.herokuapp.com/)

---

## How to Play

1. Enter your name when prompted
2. The game board will be displayed
3. Enter row and column numbers (0–4)
4. Try to locate and sink all ships
5. You win if all ships are destroyed before turns run out

---

## Features

### Game Start
- ASCII logo displayed at launch
- Welcome message and instructions
- Player name input with validation

### Game Board
- 5x5 grid displayed clearly
- Rows and columns labelled
- Updates after each move

### Gameplay
- Player selects coordinates
- Hit detection system:
  - 🎯 Hit
  - ❌ Miss
- Prevents duplicate guesses
- Turn counter system

### Win / Loss System
- Player wins by sinking all ships
- Player loses if turns run out

### Score Storage
- Game results stored in `scores.json`

### Input Validation
- Prevents empty name input
- Prevents invalid coordinates
- Handles non-numeric input

---

## User Experience (UX)

- Clean terminal layout
- Centered UI for readability
- Colour-coded feedback using `colorama`
- Clear instructions and feedback messages

---

## Technologies Used

### Languages
- Python

### Libraries
- `colorama` (for terminal styling)
- `json` (for data storage)

### Tools
- Git & GitHub (version control)
- Heroku (deployment)
- VS Code (development)

---

## Data Model

The application uses:

- Lists → game board
- Tuples → ship positions
- JSON → store game results

---

## Testing

### Manual Testing

| Feature | Expected Result | Actual Result |
|--------|--------------|--------------|
| Game loads | Logo + welcome message | Pass |
| Name input | Accept valid name | Pass |
| Empty name | Re-prompt user | Pass |
| Board display | 5x5 grid shown | Pass |
| Valid guess | Accept input | Pass |
| Invalid input | Error message | Pass |
| Duplicate guess | Warning message | Pass |
| Hit detection | Shows hit | Pass |
| Miss detection | Shows miss | Pass |
| Win condition | Game ends correctly | Pass |
| Loss condition | Game ends correctly | Pass |
| Score saving | JSON updated | Pass |

---

## Bugs

### Fixed Bugs
- Indentation errors causing crashes
- Input not working in Heroku
- Incorrect Procfile configuration
- Non-interactive terminal issue

### Known Bugs
- No option to remove previous guesses
- Ships may overlap (low probability)

---

## Deployment

### Heroku Deployment

1. Create Heroku app
2. Connect GitHub repository
3. Add buildpacks:
   - Python
   - Node.js
4. Add Procfile:
web: node index.js

5. Deploy project

---

## Version Control

- Git used for tracking changes
- Regular commits made throughout development
- GitHub used to store project repository

---

## Future Improvements

- Add multiple ship sizes
- Add difficulty levels
- Improve UI styling further
- Add leaderboard system
- Allow player to choose board size

---

## Credits

- Code Institute learning materials
- Stack Overflow (debugging help)
- Python documentation

---

## Acknowledgements

- Code Institute tutors and mentors
- Online developer community