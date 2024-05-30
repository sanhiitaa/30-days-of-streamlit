import streamlit as st

st.header("Method for the day: st.selectbox")

option = st.selectbox("what would you like to eat for the rest of your life?",
                      ('rajma-chawal', "chicken-tikka", "burger", "chinese-cuisine"),
                      help='this is a help box',
                      disabled=False)

st.write(f"you have decided to eat **{option}** for the rest of your life.")