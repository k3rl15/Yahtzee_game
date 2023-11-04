# Import the `randint` function from the `random` module.
from random import randint


# Define the main entry point for the Yahtzee game.
def main():
    """
    Main function to initiate and control the Yahtzee game.
    """
    print("YAHTZEE!")

    # Continue playing as long as the player wants.
    while True:
        play = input("\nDo you want to play? (yes/no):").lower()
        if play == 'yes':
            play_game()
        elif play == 'no':
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Define the function to play the game rounds.
def play_game():
    """
    Function to play multiple rounds of the Yahtzee game.
    """
    rounds = 0
    player = []  # List to store the player's dice rolls for each round.
    results = []  # List to store the results of each round.
    max_rounds = 3  # Set the maximum number of rounds.

    while rounds < max_rounds:
        dice = play_round()
        player.append(dice)
        round_result = roll_type(dice)
        rounds += 1
        print(f"Round {rounds}:\nFinal dice rolls: {dice}")
        print(round_result)
        print()
        results.append(round_result)

    # Display the results for each round.
    pos = 0
    for result in results:
        print(f"Round {pos + 1}:\nDices: {player[pos]}\nResults: {result}")
        pos += 1


# Define the function to play a single round.
def play_round():
    """
    Function to play a single round of the Yahtzee game.
    It collects dice rolls and returns the final dice rolls for the round.
    """
    dice = roll_dice()
    display_dice(dice)

    # Allow up to two rerolls.
    for _ in range(2):
        while True:
            try:
                indexes_to_reroll = [int(i) for i in input("Enter position of dice to reroll (e.g., 1 3 4): ").split()]
                if all(1 <= index <= 5 for index in indexes_to_reroll):
                    reroll_dice(dice, [index - 1 for index in indexes_to_reroll])
                    display_dice(dice)
                    break
                else:
                    print("Invalid input. Dice positions should be between 1 and 5.")
            except (ValueError, IndexError):
                print("Invalid input. Please input valid dice positions (e.g., 1 2 5)")

    return dice


# Define the function to determine the type of roll.
def roll_type(dice):
    """
    Function to determine the type of roll (e.g., Yahtzee, Full House) in a given set of dice rolls.
    """
    count = {}  # Dictionary to count occurrences of each dice value.

    for d in dice:
        if d in count:
            count[d] += 1
        else:
            count[d] = 1

    new_dices = set(sorted(dice))

    if 5 in count.values():
        return "Yahtzee"
    elif 4 in count.values():
        return "Four of a Kind"
    elif 3 in count.values() and 2 in count.values():
        return "Full House"
    elif 3 in count.values():
        return "Three of a Kind"
    elif len(new_dices) == 5:
        if all(dice in [1, 2, 3, 4, 5] for dice in new_dices):
            return "Low Straight"
        elif all(dice in [2, 3, 4, 5, 6] for dice in new_dices):
            return "High Straight"
    else:
        return "Nothing Special"


# Define the function to roll five dice.
def roll_dice():
    """
    Function to generate a list of 5 random dice rolls between 1 and 6 for a single round.
    """
    return [randint(1, 6) for _ in range(5)]


# Define the function to display the current dice rolls.
def display_dice(dice):
    """
    Function to display the current dice rolls to the player.
    """
    print("Your dice:", dice)


# Define the function to reroll selected dice.
def reroll_dice(dice, indexes_to_reroll):
    """
    Function to reroll selected dice based on the player's input.
    """
    for index in indexes_to_reroll:
        dice[index] = randint(1, 6)

# Check if the script is executed as the main program.
if __name__ == "__main__":
    main()  # Start the Yahtzee game.
