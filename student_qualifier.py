# Author: Angel Vaquera Jr
# File name: student_qualifier.py
# Description: This app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.

while True:
    last_name = input("Enter the student's last name (Enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(first_name + " " + last_name + " has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name + " " + last_name + " has made the Honor Roll.")
    else:
        print(first_name + " " + last_name + " has not made either the Dean's List or the Honor Roll.")
