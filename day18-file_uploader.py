import streamlit as st
import pandas as pd

st.title('Method for the day: st.file_uploader')

st.subheader('Input CSV file:')
uploaded_file= st.file_uploader('choose a file', 
                                type=['csv'],
                                accept_multiple_files=False,
                                help='a help box :3',
                                )

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.subheader('The file you uploaded: ')
    st.write(df)
    st.subheader('Descriptive statistics')
    st.write(df.describe())
else:
    st.info('upload a csv')
