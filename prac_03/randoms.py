import random

# Line 1: random.randint(5, 20)
print(random.randint(5, 20))  # Produces a random int between 5 and 20 inclusive.
# Smallest: 5, Largest: 20

# Line 2: random.randrange(3, 10, 2)
print(random.randrange(3, 10, 2))  # Produces a random odd number between 3 and 9 (3, 5, 7, 9)
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4? No, because step=2 skips even numbers.

# Line 3: random.uniform(2.5, 5.5)
print(random.uniform(2.5, 5.5))  # Produces a random float between 2.5 and 5.5
# Smallest: 2.5, Largest: 5.5

# Random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")
