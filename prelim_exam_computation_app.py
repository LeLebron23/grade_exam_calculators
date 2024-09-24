import streamlit as st

# Set page config with a black and green theme
st.set_page_config(page_title="🎮 Grade Calculator", page_icon="", layout="centered")

# Custom CSS for black and green theme
st.markdown(
    """
    <style>
    body {
        background-color: black;
        font-family: 'Arial', sans-serif;
        color: #00FF00;
    }
    .main {
        background-color: black;
    }
    h1 {
        color: #00FF00;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 40px;
        text-shadow: 2px 2px 5px #ffffff;
    }
    .stNumberInput > div > div > input {
        background-color: #444444; /* Gray textbox */
        color: #00FF00;
        font-family: 'Arial', sans-serif;
        border: 2px solid #00FF00; /* Green border */
        width: 100px; /* Smaller input box */
    }
    .stButton button {
        background-color: #00FF00; /* Green button */
        color: black;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-family: 'Arial', sans-serif;
    }
    .stButton button:hover {
        background-color: #00cc00; /* Darker green */
        color: black;
    }
    .input-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px; /* Space between boxes */
    }
    /* Hide the arrows for the number input */
    input[type=number]::-webkit-inner-spin-button,
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title(" Grade Calculator")

def calculate_midterm_final(prelim_grade, target_grade):
    prelim_weight = 0.2
    midterm_weight = 0.3
    finals_weight = 0.5

    remaining_grade = target_grade - (prelim_grade * prelim_weight)

  
    midterm_needed = remaining_grade / (midterm_weight + finals_weight) * midterm_weight
    final_needed = remaining_grade / (midterm_weight + finals_weight) * finals_weight

    return midterm_needed, final_needed


absences = st.number_input("Enter number of absences: ", min_value=0, step=1)

if absences >= 4:
    st.write("🚫 **FAILED due to absences.**")
else:
    st.markdown("<div class='input-container'>", unsafe_allow_html=True)
    prelim_exam = st.number_input("Prelim Exam Grade (0-100): ", 0.0, 100.0)
    quizzes = st.number_input("Quizzes Grade (0-100): ", 0.0, 100.0)
    requirements = st.number_input("Requirements Grade (0-100): ", 0.0, 100.0)
    recitation = st.number_input("Recitation Grade (0-100): ", 0.0, 100.0)
    st.markdown("</div>", unsafe_allow_html=True)


    attendance = 100 - (absences * 10)


    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)

  
    prelim_grade = (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)

   
    st.write(f"**Prelim Grade:** {prelim_grade:.2f}")

  
    target_pass = 75
    target_deans = 90

    midterm_needed_for_pass, final_needed_for_pass = calculate_midterm_final(prelim_grade, target_pass)
    midterm_needed_for_deans, final_needed_for_deans = calculate_midterm_final(prelim_grade, target_deans)


    st.write(f"To pass with 75% overall grade, you need a Midterm grade of {midterm_needed_for_pass:.2f} "
             f"and a Final grade of {final_needed_for_pass:.2f}.")
    
    
    st.write(f"To achieve Dean's Lister status with 90% overall grade, you need a Midterm grade of "
             f"{midterm_needed_for_deans:.2f} and a Final grade of {final_needed_for_deans:.2f}.")
