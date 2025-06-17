"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}


def main():
    state_code = input("Enter short state: ").strip().upper()
    while state_code:
        full_name = CODE_TO_NAME.get(state_code)
        if full_name:
            print(f"{state_code} is {full_name}")
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()

    print("\nAll states and abbreviations:")
    for code, name in CODE_TO_NAME.items():
        print(f"{code:<3} is {name}")


if __name__ == "__main__":
    main()
