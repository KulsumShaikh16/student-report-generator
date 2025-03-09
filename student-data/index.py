
import streamlit as st

st.title("Student Report Generator")
def calculate_grade(percentage):
    if 80 <= percentage:
        return "A+"
    elif 70 <= percentage :
        return "A"
    elif 60 <= percentage :
        return "B"
    elif 50 <= percentage :
        return "c"
    elif 40 <= percentage :
        return "D"
    else:
        return "Fail"

def generate_report_card(students):
    print("\n----- 📝 Student Report Cards 📝 -----")
    
    i = 0  # Starting index for the while loop
    while i < len(students):
        student = students[i]
        name = student['name']
        roll = student['roll']
        marks = student['marks']
        total_marks = sum(marks.values())
        percentage = (total_marks / 500) * 100
        grade = calculate_grade(percentage)

        print("\n-------------------------------------")
        print(f"Name        : {name}")
        print(f"Roll Number : {roll}")
        print("-------------------------------------")
        for subject, mark in marks.items():
            print(f"{subject:<10}: {mark}")
        print("-------------------------------------")
        print(f"Total Marks : {total_marks} / 500")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Grade       : {grade}")
        print("-------------------------------------")
        
        i += 1  # Move to the next student

# Main function to collect data and control program flow
def main():
    students = []

    while True:
        try:
            name = input("Enter Student Name: ")
            roll = input("Enter Roll Number: ")
            marks = {}
            subjects = ["Math", "Physics", "Urdu", "English", "Computer"]

            for subject in subjects:
                while True:
                    try:
                        mark = int(input(f"Enter marks for {subject}: "))
                        if 0 <= mark <= 100:
                            marks[subject] = mark
                            break
                        else:
                            print("Marks should be between 0 and 100.")
                    except ValueError:
                        print("Invalid input! Please enter a valid number.")

            students.append({'name': name, 'roll': roll, 'marks': marks})
            print(f"\nRecord of {name} inserted successfully.")

            choice = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().upper()
            if choice == 'N':
                break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    if students:
        generate_report_card(students)
    else:
        print("No student data entered. Exiting the program.")

# Run the main function
main()

