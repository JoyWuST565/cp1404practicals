"""
Emails
Estimate: 30 minutes
Actual:   49 minutes
"""


def get_name_from_email(email: str) -> str:
    prefix = email.split("@")[0]
    parts = prefix.replace("_", ".").split(".")
    return " ".join(part for part in parts if part).title()


def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        default_name = get_name_from_email(email)
        response = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if response and response not in ("y", "yes"):
            name = input("Name: ").strip().title()
        else:
            name = default_name

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
