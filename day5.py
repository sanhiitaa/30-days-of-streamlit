import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# exmaple 1
st.write('Hello, *World!* :sunglasses:')

# example 2
st.write(1234)

# example 3
df=pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [6,7,8,9,10]
})

st.write(df)

# example 4
st.write('Below is a dataframe', df, 'Above is a dataframe.')

# example 5
df2= pd.DataFrame(np.random.randn(200, 3),
                  columns=['a', 'b', 'c'])

c=alt.Chart(df2).mark_circle().encode(x='a',
                                      y='b',
                                      size='c',
                                      color='c',
                                      tooltip=['a', 'b', 'c'])

st.write(c)

st.write(df2)

st.markdown('# Hello World - markdown')
st.header('Hello World- header')
st.subheader('Hello World- subheader')
st.caption('Hello World- caption')
st.text('Hello World- text')
st.latex('Hello World- latex')
st.code('Hello World- code')