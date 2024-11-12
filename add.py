import streamlit as st

# Title and description with colorful text using markdown
st.markdown("<h1 style='color: #ff6347;'>🌈 Fun Adding App for Toddlers</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4682b4;'>Let's add two numbers together!</h3>", unsafe_allow_html=True)

# Ask for the first number
first_number = st.number_input("Enter the first number:", min_value=0, step=1, format="%d")

# Ask for the second number
second_number = st.number_input("Enter the second number:", min_value=0, step=1, format="%d")

# Calculate the sum
result = first_number + second_number

# Display the result with colorful output
st.markdown(f"<h2 style='color: #32cd32;'>The sum is: {result}</h2>", unsafe_allow_html=True)
