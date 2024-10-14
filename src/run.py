# import streamlist
import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np   
import matplotlib.pyplot as plt

st.title(':desktop_computer: pytopia-dashboard')

with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(1000), ax=ax)
    st.pyplot(fig)
