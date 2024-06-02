import streamlit as st

st.title('Theming with config.toml!')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code('''
        [theme]
        primaryColor="#F39C12"
        backgroundColor="#2E86C1"
        secondayBackgroundColor="#AED6F1"
        textColor="#FFFFFF"
        font="monospace"
        ''')

number= st.select_slider('Select a genre:',
                         options=['thriller', 'horror', 'romance', 'sci-fi'])
st.write('your chosen genre is: ', number)

