import streamlit as st

st.header('Method for the day: st.checkbox')

st.write('What do you wish for?')

job= st.checkbox('Job, duh!')
icecream= st.checkbox('Icecream')
vacation= st.checkbox('A much needed vacay')
food= st.checkbox('Food, because i am always hungry')

if job:
    st.write("there you go, A JOB!")
elif icecream:
    st.write("there you go, AN ICECREAM!")
elif vacation:
    st.write("there you go, A VACATION!")
elif food:
    st.write("there you go, LOTSA FOOD!")