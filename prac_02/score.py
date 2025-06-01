import random


def determine_score_result(score):
    """Return result string based on score."""
    if 0 <= score <= 100:
        if score < 50:
            return "Bad"
        elif score < 90:
            return "Passable"
        else:
            return "Excellent"
    else:
        return "Invalid score"


def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(determine_score_result(random_score))


main()
