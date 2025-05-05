import random
# Check that users have entered a valid option based on a list

def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:
        user_response = input(question).lower()
        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# Displays instructions

def instructions():
    """ Prints the instructions for the user """
    print("""
*** Instructions ****

To begin, choose the number of rounds (or press enter for infinite mode).

The play against the computer. You need to choose on of the following: R (rock), P (paper), or S (scissors).

The rules are as follows:
o  Paper beats rock
o  Rock beats scissors
o  Scissors beats paper

Good Luck!
    """)


# Check for an integer more than 0, also allows <enter>


def int_check(question):
    """Checks users enter an integer that is 1 or more."""
    # User input
    while True:
        # Error message
        error = f"Please enter an integer that is 1 or more.."

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"
        try:
            response = int(to_check)
            if response < 1:
               print(error)
            else:
              return response
        except ValueError:
             print(error)

# compares user / computer choice and returns
# result (win / lose / tie)
def rps_compare(user, comp):
    # If the user and the computer choice is the same, the game result is a tie
    if user == comp:
        round_result = "tie"
    # There are three ways to win
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    # Otherwise, it's a loss
    else:
        round_result = "lose"
    return round_result

# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# Instructions
# Ask the user if they would like to see the instructions
want_instructions = string_checker("Do you want to read the instructions? ")
print(f"you chose {want_instructions}")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
# Ask user for the number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings - Based on selected mode
    if mode =="infinite":
        rounds_heading = f"\n∞∞∞ Round {rounds_played + 1} (Infinite Mode) ∞∞∞"
    else:
        rounds_heading = f"\n📀📀📀 Round {rounds_played + 1} of {num_rounds} 📀📀📀"

    print(rounds_heading)
    print()

    # Allows computer to randomly choose a move from the rps list, minus the exit code
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice:", comp_choice)

    # Collect users chosen move
    users_choice = string_checker("Choose: ", rps_list)
    print("You chose", users_choice)

    if users_choice == "xxx":
        break


    result = rps_compare(users_choice, comp_choice)

    # Adjust game lost / game tied counters and add results
    if result == "tie":
        rounds_tied += 1
        feedback = "🪢🪢🪢 It's a tie! 🪢🪢🪢"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😔😔😔 You lost! 😔😔😔"
    else:
        feedback = "👍👍👍 You won! 👍👍👍"

    # Set up round feedback and output it to user
    # Add it top the game history list (Including Round number)
    round_feedback = f"{users_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round {rounds_played + 1} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1



# Game loop ends here

# Game history / statistics area

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output game statistics
    print()
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t"
          f"😔 Lost: {percent_lost:.2f} \t"
          f"🪢 Tied: {percent_tied:.2f}")

    # Ask user if they would like to see their game history and output if they request to
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)
    print()
    print("thanks for playing.")
else:
    print("🐔🐔🐔 Oops! You chickened out and did not play any rounds 🐔🐔🐔")