import streamlit as st
import pandas as pd

st.title("Student Report Generator")

def calculate_grade(percentage):
    if 80 <= percentage:
        return "A+"
    elif 70 <= percentage:
        return "A"
    elif 60 <= percentage:
        return "B"
    elif 50 <= percentage:
        return "C"
    elif 40 <= percentage:
        return "D"
    else:
        return "Fail"

def generate_report_card(students):
    st.subheader("📝 Student Report Cards 📝")
    for student in students:
        name = student['name']
        roll = student['roll']
        marks = student['marks']
        total_marks = sum(marks.values())
        percentage = (total_marks / 500) * 100
        grade = calculate_grade(percentage)

        st.markdown("---")
        st.write(f"**Name:** {name}")
        st.write(f"**Roll Number:** {roll}")
        st.markdown("---")
        for subject, mark in marks.items():
            st.write(f"**{subject}:** {mark}")
        st.markdown("---")
        st.write(f"**Total Marks:** {total_marks} / 500")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")
        st.markdown("---")

# Main function to collect data
def main():
    students = []
    num_students = st.number_input("How many students' data you want to enter?", min_value=1, step=1)

    for _ in range(num_students):
        st.markdown("### Enter Student Details")
        name = st.text_input("Enter Student Name:")
        roll = st.text_input("Enter Roll Number:")
        marks = {}
        subjects = ["Math", "Physics", "Urdu", "English", "Computer"]

        for subject in subjects:
            mark = st.number_input(f"Enter marks for {subject}:", min_value=0, max_value=100, step=1)
            marks[subject] = mark

        if st.button("Add Record"):
            students.append({'name': name, 'roll': roll, 'marks': marks})
            st.success(f"Record of {name} inserted successfully!")

    if students:
        generate_report_card(students)
    else:
        st.warning("No student data entered yet.")

# Run the main function
if __name__ == "__main__":
    main()
