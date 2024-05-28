import streamlit as st
from datetime import time, datetime

st.header('Method for the day: st.slider')

# example 1
st.subheader('1. Simple Slider')

age=st.slider('Your age?', 0, 130, 0) # (text, start-point, end-point, default-point-of-slider)
st.write('I am ', age, ' years old.')

# example 2
st. subheader('2. Range Slider')

values= st.slider('select a range of values: ',
                  0.0, 100.0, (25.0, 75.0)) # (text, start-point, end-point, (left-default-point, right-default-point))
st.write('values: ', values)

# example 3
st.header('3. Datetime slider')

start_time=st.slider('when do you start? ',
                     min_value = datetime(2019, 6, 18, 0, 0),
                     max_value = datetime(2020, 6, 18, 23, 59),                    
                     value = datetime(2020, 1, 1, 0, 0), # datetime=(year, month, day, hour, minute)
                     format='MM/DD/YY - hh:mm')
st.write('start time: ', start_time)

# example 4
st.subheader('4. Range Time Slider')

appointment= st.slider('schedule your appointment: ',
                       value=(time(11,30), time(12, 45)))

start_time= appointment[0].strftime('%I:%M %p')
end_time= appointment[1].strftime('%I:%M %p')

st.write('you are scheduled for: ', start_time, ' to ', end_time)

st.header('Method #2: st.select_slider')
st.write('Accepts any datatype and takes an iterable set of options')

# example 6
color = st.select_slider('Select a color: ',
                         options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('the color you selected is: ', color)

# example 7 - two options (at max)
start_color, end_color = st.select_slider('Select a color: ',
                         options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
                         value=('red', 'violet'))
st.write('the color you selected is: ', start_color, "and", end_color)
