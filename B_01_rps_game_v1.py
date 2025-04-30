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


# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# Instructions

# Ask user for the number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
if num_rounds == "infinite":
    mode = "infinite"
    print("you chose infinite")
    num_rounds = 5
# Game loop starts here
while rounds_played < num_rounds:
    users_choice = input("Choose: ")

    if users_choice == "xxx":
        break
    rounds_played += 1
    print("Rounds played: ", rounds_played)
    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    print("Number of rounds: ", num_rounds)


# Game loop ends here

# Game history / statistics area