import streamlit as st

st.title("Student Report Generator")

# calculate percentage
def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

# Report card
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
        st.write(f"**Total Marks:** {total_marks} / 500")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")
        st.markdown("---")

# input from user
students = []
num_students = st.number_input("How many students?", min_value=1, step=1)

for i in range(num_students):
    st.markdown(f"### Enter Details for Student {i + 1}")
    name = st.text_input("Name:", key=f"name_{i}")
    roll = st.text_input("Roll Number:", key=f"roll_{i}")
    marks = {subject: st.number_input(f"{subject} Marks:", 0, 100, key=f"{subject}_{i}") 
             for subject in ["Math", "Physics", "Urdu", "English", "Computer"]}

    if st.button("Add Record", key=f"add_{i}"):
        students.append({'name': name, 'roll': roll, 'marks': marks})
        st.success(f"Record of {name} added!")

if students:
    generate_report_card(students)
else:
    st.info("Enter student data to generate report cards.")
