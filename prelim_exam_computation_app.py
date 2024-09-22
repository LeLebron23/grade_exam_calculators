import streamlit as st

# Set page config with a Roblox-themed emoji icon
st.set_page_config(page_title="🎮 Grade Calculator", page_icon="🕹️", layout="centered")

# Custom CSS for Roblox theme
st.markdown(
    """
    <style>
    body {
        background-color: #ffcc00; /* Roblox yellow */
        font-family: 'Arial', sans-serif;
        color: #000000;
    }
    .main {
        background-color: #ffcc00;
    }
    h1 {
        color: #d00000; /* Roblox red */
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 40px;
        text-shadow: 2px 2px 5px #ffffff;
    }
    .stNumberInput > div > div > input {
        background-color: #ffffff;
        color: #000000;
        font-family: 'Arial', sans-serif;
        border: 2px solid #d00000; /* Roblox red */
    }
    .stButton button {
        background-color: #d00000; /* Roblox red */
        color: #ffffff;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-family: 'Arial', sans-serif;
    }
    .stButton button:hover {
        background-color: #a00000; /* Darker red */
        color: #ffffff;
    }
    .stNumberInput div {
        font-family: 'Arial', sans-serif;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with Roblox theme
st.title("🎮 Grade Calculator")

# Function to calculate required midterm and final grades
def calculate_midterm_final(prelim_grade, target_grade):
    prelim_weight = 0.2
    midterm_weight = 0.3
    finals_weight = 0.5

    # Remaining grade needed after prelims
    remaining_grade = target_grade - (prelim_grade * prelim_weight)

    # Let Midterm and Finals have equal contribution
    midterm_needed = remaining_grade / (midterm_weight + finals_weight) * midterm_weight
    final_needed = remaining_grade / (midterm_weight + finals_weight) * finals_weight

    return midterm_needed, final_needed

# Input fields
absences = st.number_input("Enter number of absences: ", min_value=0, step=1)

if absences >= 4:
    st.write("🚫 **FAILED due to absences.**")
else:
    prelim_exam = st.number_input("Enter Prelim Exam Grade (0-100): ", 0.0, 100.0)
    quizzes = st.number_input("Enter Quizzes Grade (0-100): ", 0.0, 100.0)
    requirements = st.number_input("Enter Requirements Grade (0-100): ", 0.0, 100.0)
    recitation = st.number_input("Enter Recitation Grade (0-100): ", 0.0, 100.0)

    # Attendance calculation
    attendance = 100 - (absences * 10)

    # Class standing calculation
    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)

    # Prelim Grade calculation
    prelim_grade = (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)

    # Display calculated Prelim Grade
    st.write(f"**Prelim Grade:** {prelim_grade:.2f}")

    # Calculate required midterm and finals to pass or achieve Dean's Lister
    target_pass = 75
    target_deans = 90

    midterm_needed_for_pass, final_needed_for_pass = calculate_midterm_final(prelim_grade, target_pass)
    midterm_needed_for_deans, final_needed_for_deans = calculate_midterm_final(prelim_grade, target_deans)

    # Display required midterm and final grades for passing
    st.write(f"To pass with 75% overall grade, you need a Midterm grade of {midterm_needed_for_pass:.2f} "
             f"and a Final grade of {final_needed_for_pass:.2f}.")
    
    # Display required midterm and final grades for Dean's Lister
    st.write(f"To achieve Dean's Lister status with 90% overall grade, you need a Midterm grade of "
             f"{midterm_needed_for_deans:.2f} and a Final grade of {final_needed_for_deans:.2f}.")
