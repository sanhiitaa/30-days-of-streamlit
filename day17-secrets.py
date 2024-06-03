import streamlit as st

st.title('Method for the Day: st.secrets')

# Corrected key to match secrets.toml
st.write(st.secrets['message'])

# steps
st.write('Steps')

st.markdown("1. make a .streamlit/secrets.toml file\n"
         '''2. define your secret message there: `message="My secret message"` \n'''
         '''3. in your app file write: `st.write(st.secrets['message'])` \n'''
         '''4. run the app :) \n'''
           "5. used to store passwords, API keys, and other sensitive info, that can later be utilized to autheticate and authorize access to resources")
