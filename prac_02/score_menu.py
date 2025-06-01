def determine_score_result(score):
    if 0 <= score <= 100:
        if score < 50:
            return "Bad"
        elif score < 90:
            return "Passable"
        else:
            return "Excellent"
    else:
        return "Invalid score"


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def show_stars(score):
    print("*" * int(score))


def main():
    score = get_valid_score()
    menu = """\nMenu:
(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()

    print("Farewell! Thank you for using the score checker.")


main()
