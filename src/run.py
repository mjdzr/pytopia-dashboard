# import streamlist
import streamlit as st
from io import StringIO
import json

st.title(':desktop_computer: pytopia-dashboard')
st.markdown('Practice #1 of git course from pytopia.ai')

st.header("Welcome!")
st.code("""print("Hello, World!")""")

# add file uploader header 
with st.expander("Input"):
    st.header("File uploader")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        data = json.loads(string_data)
        #t.json(data)
        st.json(data['audio_features'][0])

