# Yahtzee Game

The Yahtzee Game is a text-based Python script that allows you to play a simplified version of the classic dice game Yahtzee. In Yahtzee, the objective is to achieve various combinations of dice rolls and score points. This script provides a basic implementation of the game and allows you to play multiple rounds.

## Getting Started

To play the Yahtzee game, follow these instructions:

1. Make sure you have Python installed on your computer.

2. Download the `yahtzee_game.py` script.

3. Run the script using the following command:
   - Using a terminal, first navigate to the script's directory (for example, `cd /path/to/yahtzee_game`) and then run the script:
   ```
   python yahtzee_game.py
   ```

4. Follow the on-screen prompts to play the game. You can choose to play multiple rounds, and the script will display the results of each round.

## How to Play

- The game allows you to play up to three rounds, each with three opportunities to reroll dice.

- On each turn, you'll roll five dice. You can choose which dice to reroll (up to three times) to achieve different combinations and maximize your score.

- After each turn, the script will display the result of the round, including the combination achieved.

- The game supports various combinations, such as "Yahtzee," "Four of a Kind," "Full House," and more. 

- To exit the game, simply type "no" when asked if you want to play again.

## Code Structure

- The script is organized into several functions, making it easy to understand and modify:

  - `main()`: The entry point of the game that controls the flow.
  - `play_game()`: Manages multiple rounds of the game.
  - `play_round()`: Handles a single round of dice rolling and rerolls.
  - `roll_type()`: Determines the type of roll (combination) achieved in a set of dice.
  - `roll_dice()`: Generates five random dice rolls.
  - `display_dice()`: Displays the current dice rolls.
  - `reroll_dice()`: Allows the player to reroll selected dice.
