import streamlit as st

# 1. Title
st.title("Student Grade Dashboard")
st.subheader("Choose Input Method")
input_method = st.radio(
    "Select how you want to enter marks:",
    ["Slider", "Number Input"]
)

if input_method == "Slider":
    marks = st.slider(
        "Select Marks",
        min_value=0,
        max_value=100,
        value=50
    )

else:
    marks = st.number_input(
        "Enter Marks",
        min_value=0,
        max_value=100,
        value=50
    )

if st.button("Calculate Grade"):
    if 90<= marks <= 100:
            grade = 'A'
            status = "First Class"
            Message = st.success("Excellent Performance! 🎉")
    elif 80<= marks < 90:
            grade = 'B'
            status = "First Class"
            Message = st.success("Very Good!")

    elif 70<= marks < 80:
            grade = 'C'
            status = "Second Class"
            Message = st.warning("Good, but room for improvement.")
    elif 60<= marks < 70:
            grade = 'D'
            status = "Second Class"
            Message = st.warning("Good, but room for improvement.")
    else:   
            grade = 'E'
            status = "Third Class"
            Message = st.warning("Need Improvement")

    st.write("Result")
    st.write(f"Marks Obtained: {marks}")
    st.write(f"Grade: {grade}")
    st.info(status)
