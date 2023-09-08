import streamlit as st

st.title("The Mean of Student Degrees")
st.write("Enter the degree for each subject.")

number_subjects = st.number_input(
    "Insert The Number of Subjects", min_value=1, step=1, value=1)

list_degrees = []

for subject in range(number_subjects):
    degree = st.number_input(
        f"Enter degree for Subject {subject+1}", min_value=0.0, step=0.1, value=0.0)
    list_degrees.append(degree)

if st.button("Calculate the Mean"):
    total_degrees = sum(list_degrees)
    num_degrees = len(list_degrees)
    mean = total_degrees / num_degrees
    st.write(f"The mean degree is: {mean:.2f}")
