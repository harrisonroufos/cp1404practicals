"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)


def display_subject_details(subject_data: list):
    """Display subject details from list"""
    for subject, teacher, number_of_students in subject_data:
        print(f"{subject} is taught by {teacher:12} and has {number_of_students:4} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data


main()

