import streamlit as st

st.header("Method for the day: st.multiselect")

option = st.multiselect("what two elements describe you the best?",
                        ['fire', 'water', 'air', 'earth', "space"],
                        max_selections=5,
                        placeholder='choose an option')

st.write(f"the two elements that best describe you are {option}")