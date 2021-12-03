import streamlit as st
import numpy as np
import pandas as pd

st.title('This is my first app from Galileo Master!')

x = 4
st.write(x,'^2 = ', x**2)


st.write(pd.DataFrame({
    'Column A': ['A','B', 'C'],
    'Column B': ['1','2', '3'],
}))

df_to_plot = pd.DataFrame(
    np.random.randn(20, 3), columns =['A', 'B', 'C']
)

st.line_chart(df_to_plot)

df_lat_lon = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.44],
    columns=['lat', 'lon']
)

st.map(df_lat_lon)

if st.checkbox('show dataframe'):
    df_lat_lon


##Widgets

x = st.slider('select a value for X')
y = st.slider('select a power for X')
st.write(x, 'CUBE IS ', x**y)

option_list = [1,2,3,4,5,6,7,8,9,10]
option = st.selectbox('Which number do you like best?', option_list)

st.write('Your favorite option is : ', option)


import time

label = st.empty()
progress_bar = st.progress(0)

for i in range(0,101):
    label.text(f'the value is:{i}%')
    progress_bar.progress(i)
    time.sleep(0.01)

label.text(f'the wait is done')

st.sidebar.write("This is a sidebar")
option2 = st.sidebar.selectbox('Which number do you like best?22', option_list)

st.sidebar.write('Another Slider')
another_slider = st.sidebar.slider('Select range', 0.0, 100.0, (25.0,75.0))