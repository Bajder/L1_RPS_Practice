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

rps_list = ["rock", "paper", "scissors", "xxx"]

want_instructions = string_checker("Do you want to see the instructions? ")
print("You chose: ", want_instructions)

user_choice = string_checker("Choose: ",
                             rps_list)

print("You chose: ", user_choice)
