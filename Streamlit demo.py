import streamlit as st
import requests
import json
import pandas as pd

response = requests.get("https://api.covid19india.org/data.json")
print(response.json())

@st.cache
def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    return(text)

df = pd.read_json(jprint(response.json()['statewise']))

### Print message on screen ###

st.title('My first app')

st.write(df)


st.markdown("This next word will appear in bold : **_markdown**")

### Create slider on screen ###

if st.button('say hello'):
    st.write('helo')
else:
    st.write('goodbye')

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write('Not Great!')
    
    

x = st.slider('x')
st.write(x, " squared is", x * x)


