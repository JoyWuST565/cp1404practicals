"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_data()
    display_subject_details(subjects)


def load_data():
    subjects = []
    with open(FILENAME) as input_file:
        for line in input_file:
            subject_code, lecturer, students = line.strip().split(',')
            subjects.append([subject_code, lecturer, int(students)])
    return subjects


def display_subject_details(subjects):
    for subject_code, lecturer, student_count in subjects:
        print(f"{subject_code} is taught by {lecturer:<20} and has {student_count:>3} students")


if __name__ == "__main__":
    main()
