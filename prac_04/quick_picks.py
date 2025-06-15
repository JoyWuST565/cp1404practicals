import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        pick = generate_pick()
        print(" ".join(f"{n:2}" for n in pick))


def generate_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        candidate = random.randint(MIN_NUMBER, MAX_NUMBER)
        if candidate not in numbers:
            numbers.append(candidate)
    return sorted(numbers)


if __name__ == "__main__":
    main()
