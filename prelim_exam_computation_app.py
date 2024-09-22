import streamlit as st

# Set page config with Minecraft-style emoji icon
st.set_page_config(page_title="Minecraft Grade Calculator", page_icon="🟫", layout="centered")

# Custom CSS for Minecraft theme
st.markdown(
    """
    <style>
    body {
        background-color: #c2b280;
        font-family: 'Press Start 2P', cursive;
    }
    .main {
        background-color: #c2b280;
    }
    h1 {
        color: #1E1E1E;
        text-align: center;
        font-family: 'Press Start 2P', cursive;
        font-size: 24px;
    }
    .stNumberInput > div > div > input {
        background-color: #f0e68c;
        color: #1E1E1E;
        font-family: 'Press Start 2P', cursive;
        border: 2px solid #1E1E1E;
        border-radius: 0;
    }
    .stButton button {
        background-color: #8B4513;
        color: white;
        border-radius: 0;
        padding: 10px 20px;
        border: 2px solid #1E1E1E;
        font-family: 'Press Start 2P', cursive;
    }
    .stButton button:hover {
        background-color: #A0522D;
        color: white;
    }
    .stNumberInput div {
        font-family: 'Press Start 2P', cursive;
    }
    </style>

    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Title in Minecraft theme
st.title("🟫 Minecraft Grade Calculator 🟫")

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
absences = st.number_input("🟩 Enter number of absences: ", min_value=0, step=1)

if absences >= 4:
    st.write("💀 **FAILED due to absences.**")
else:
    prelim_exam = st.number_input("📜 Enter Prelim Exam Grade (0-100): ", 0.0, 100.0)
    quizzes = st.number_input("📚 Enter Quizzes Grade (0-100): ", 0.0, 100.0)
    requirements = st.number_input("🛠️ Enter Requirements Grade (0-100): ", 0.0, 100.0)
    recitation = st.number_input("🎤 Enter Recitation Grade (0-100): ", 0.0, 100.0)

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
    st.write(f"🎯 To pass with 75% overall grade, you need a Midterm grade of {midterm_needed_for_pass:.2f} "
             f"and a Final grade of {final_needed_for_pass:.2f}.")
    
    # Display required midterm and final grades for Dean's Lister
    st.write(f"🏅 To achieve Dean's Lister status with 90% overall grade, you need a Midterm grade of "
             f"{midterm_needed_for_deans:.2f} and a Final grade of {final_needed_for_deans:.2f}.")
