import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

st.title('test')
st.caption('this is')

image = Image.open('./data/test_sup.png')
st.image(image, width=200)



