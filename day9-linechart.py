# importing the library
import streamlit as st
import pandas as pd
import numpy as np

# header #1
st.header('Method for the day: st.line_chart')

# defining the line chart
chart_data= pd.DataFrame(np.random.randn(50, 3),
                         columns=['a', 'b', 'c'])

# plotting the line chart
st.line_chart(chart_data)

# header #2
st.header('Method #2: st.altair_chart')

# import the library
import altair as alt

# define how chart_data will be displayed
c= (alt.Chart(chart_data).mark_circle().encode(x='a',
                                               y='b',
                                               size='c',
                                               color='c',
                                               tooltip=["a", "b", "c"]
                                               ))

# plotting the chart
st.altair_chart(c, use_container_width=True)