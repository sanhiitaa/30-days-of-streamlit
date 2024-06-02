import streamlit as st

st.header('Method for the day: st.latex')

st.latex(r'''\text{Cost} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p w_j^2
''', help='Cost function for Ridge Regression')