"""
Wimbledon
Estimate: 30 minutes
Actual:   46 minutes
"""

FILENAME = "wimbledon.csv"


def load_wimbledon_data(filename: str) -> list[list[str]]:
    with open(filename, mode="r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        return [line.strip().split(",") for line in lines]


def count_champions(data: list[list[str]]) -> dict[str, int]:
    champion_to_wins: dict[str, int] = {}
    for row in data:
        champion = row[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_countries(data: list[list[str]]) -> set[str]:
    return {row[1] for row in data}


def main():
    wimbledon_data = load_wimbledon_data(FILENAME)

    champion_to_wins = count_champions(wimbledon_data)
    countries = extract_countries(wimbledon_data)

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins):
        print(f"{champion:20} {champion_to_wins[champion]}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
