"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError occurs if the user inputs something that is not a valid integer,
     such as a letter or a special character, when prompted for the numerator or denominator.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError occurs if the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by using a loop to repeatedly ask for a valid (non-zero) denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))

    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
