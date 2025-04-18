# Check that users have entered a valid option based on a list

while True:
    try:
        game_goal = int(input("What is the game goal? "))
        if game_goal < 13:
            print(error)
        else:
            print(f"Game goal: {game_goal}")
            break
    except ValueError:
        print(error)


# Automated testing is below in the form (test_case, expected_value)
to_test = [
    ("yes", "yes"),
    ("Y", "yes"),
    ("No", "no"),
    ("N", "no"),
    ("YeS", "yes"),
    ("Maybe", "invalid")
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, valid_ans=["yes", "no"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f" ❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
