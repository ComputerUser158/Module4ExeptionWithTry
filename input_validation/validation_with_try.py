"""
author: Rawley Collins
prompts 3 scores and returns average to the user
"""
NUMBER_TESTS = 3


def average(score1, score2, score3):
    if score1 < 0 or score2 < 0 or score3 < 0:
        raise ValueError
    return float(score1 + score2 + score3)/NUMBER_TESTS


if __name__ == "__main__":
    lastName = input("enter your last name: ")
    firstName = input("enter your first name: ")
    age = input("enter your age: ")
    firstScore = input("enter your first score: ")
    secondScore = input("enter your second score: ")
    thirdScore = input("enter your third score: ")
    try:
        average_scores = average(int(firstScore), int(secondScore), int(thirdScore))
    except ValueError:
        print("please enter only positive scores")
    else:
        print("{}, {} age: {} average grade: {}".format(lastName, firstName, age, average_scores))
