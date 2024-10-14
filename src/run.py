# import streamlist
import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np   
import matplotlib.pyplot as plt
from PIL import Image

# Login or sign up
login_option = st.sidebar.radio('Login or Sign Up', ['login', 'sign up'])

if login_option == 'login':
    with st.sidebar.form("login"):
        st.write("Login Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")


        # Every form must have a submit button.
        submitted = st.form_submit_button("login")
        if submitted:
            pass

else:
    with st.sidebar.form("sign up"):
        st.write("Sign Up Here.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("sign up")
        if submitted:
            pass

# Page header
banner = Image.open('input/banner.png')
st.image(banner, use_column_width=True)
st.title(':desktop_computer: pytopia-dashboard')

# Number metrics
st.metric(label='Number of Members', value=3000, delta = "-100")

# User profile
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Your name:', key='name_input')
    col2.text_input('Your age:', key='age_input')
    st.camera_input('Camera Input', key='camera_input')

# Statistics
with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(1000), ax=ax)
    st.pyplot(fig)

