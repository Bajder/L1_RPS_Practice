# * * * * * * * * * * * * * * * * * * *
# * Name: RPS 13 yes / no checker     *
# * Author: Brooke Jackson            *
# * Purpose: Check if user would like *
# * to see the instructions for the   *
# * game                              *
# * * * * * * * * * * * * * * * * * * *
# Ask if they want the instructions

# Check whether they said yes or no, complete functions
def yes_no(question):
    """ Checks user response the a question is yes / no (y/n), returns 'yes' or 'no' """
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter a valid input")


def instructions():
    """ Prints the instructions for the user """
    print("""
*** Instructions ****
Roll the dice and try to win!  
    """)


# MAIN ROUTINE

want_instructions = yes_no("Do you want to see the instructions? ").lower()
print(f"you chose {want_instructions}")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
print()
print("Program continues")
