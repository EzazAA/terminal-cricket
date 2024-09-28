Here's a clean, well-structured version of your `README.md` file for your cricket terminal game:

---

# Cricket Terminal Game

A simple terminal-based cricket game where you can bat and bowl against the computer. Challenge the CPU in this fun, quick game of hand-cricket right from your terminal!

## Features

- Play a text-based cricket game in your terminal.
- Choose between batting and bowling.
- Randomized decisions by the computer to simulate a real cricket match.
- Colorful output to enhance the gaming experience (using `colorama`).

## Requirements

- **Python** 3.6 or higher
- **colorama** library (for colorful terminal outputs)

## Installation

Follow these steps to install and play the game on your local machine:

1. **Clone the repository** or download the game files:

   ```bash
   git clone https://github.com/ezazaa/terminal-cricket.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd terminal-cricket
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the game** (package it locally):

   ```bash
   pip install .
   ```

## Running the Game

Once the game is installed, you can run it using the following command in your terminal:

```bash
cricket
```

Follow the on-screen instructions to start playing!

## How to Play

- **Batting**: 
  - You'll be prompted to choose a number between 1 and 6 (like cricket runs). 
  - The computer will randomly choose a number. 
  - If both numbers match, you're out. Otherwise, you score runs equal to your choice.

- **Bowling**: 
  - You choose a number between 1 and 6 to bowl. 
  - The computer will randomly choose a number for its batting. 
  - If both numbers match, the computer is out. Otherwise, the computer scores.

After both batting and bowling, the game will calculate the final score, and the winner will be announced.

## Example Gameplay

```
Choose batting(1) or bowling(2): 1
=============================================================
Now your batting
Choose any number between 1 and 6: 3
You batted for 3 and computer bowled 2
You got 3 runs
Your current score: 3
...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

## Author

**Ezaz Alam Ahmed**  
[GitHub](https://github.com/ezazaa)

---
