COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
}


def main():
    colour_name = input("Enter colour name: ").strip().lower()
    while colour_name:
        hex_code = COLOUR_TO_HEX.get(colour_name)
        if hex_code:
            print(f"{colour_name.title()} is {hex_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").strip().lower()

    print("\nAll colour names and codes:")
    for name, code in COLOUR_TO_HEX.items():
        print(f"{name.title():<15} -> {code}")


if __name__ == "__main__":
    main()
