import streamlit as st
import requests
import json
response = requests.get("https://api.covid19india.org/data.json")
print(response.json())


def jprint(obj):
    text = json.dumps(obj, sort_keys = True, indent = 4)
    return(text)

y = jprint(response.json()['statewise'])


### Print message on screen ###
st.write(y)

### Create slider on screen ###
x = st.slider('x')
st.write(x, " squared is", x * x)


