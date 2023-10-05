import streamlit as st
import pandas as pd


l = [1,23,3,4,4]
st.write(l)



st.write("ok done :a")
'Displaying using magic: smile:'
st.sidebar.slider("test")
with st.form(key="a"):
    in1 = st.text_input(label="some label")
   # st.camera_input(label="ab")
    option = st.selectbox(
    'select options?',
    ('Email', 'Home phone', 'Mobile phone'))
    submit = st.form_submit_button(label="submit")
    if submit:
        result = f'ok {in1}'
        st.write(result)
