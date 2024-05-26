import streamlit as st

st.header("Let's create a button")

if st.button ('Hi, I am a button'):
    st.write('Why hello there stranger!')

elif st.button('Hi, I am button #2'):
    st.write('I wonder what was wrong with button 1')

else:
    st.write('Jeez okay no buttons!')