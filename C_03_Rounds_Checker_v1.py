# Check that users have entered a valid option based on a list
def int_check():
    """Checks users enter an integer more than / equal to 13"""
    # Error message
    error = f"Please enter an integer more than / equal to 13."
    # User input
    while True:
        try:
            response = int(input("What is the game goal? "))
            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ("xlii", "invalid"),
    ("0.5", "invalid"),
    ("0", "invalid"),
    ("1", "1"),
    ("2", "2"),
    ("", "infinite")
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_check(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f" ❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
