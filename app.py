import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

########## Title and text ##########
st.title('Hello World!')
st.write('This is a simple example of a Streamlit app.')

########## Radio button for status ##########
status = st.radio('Set status', ['Success', 'Failed'])
placeholder = st.empty()

if status == 'Success':
    placeholder.success('Success!')
else:
    placeholder.error('Failed!')

########## Message boxes ##########
st.info('This is an informational message')

st.success('This is a success message')

st.warning('This is a warning message')

st.error('This is an error message')

########## Area chart ##########
st.header('Area Chart')
chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
st.area_chart(chart_data)

########## Altair chart ##########
st.header('Altair Chart')
source = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

chart_data_2 = alt.Chart(source).mark_circle().encode(
    x='flipper_length_mm',
    y='bill_length_mm',
    color='species',
    tooltip=['species', 'bill_length_mm', 'flipper_length_mm']
).interactive()

st.altair_chart(chart_data_2, use_container_width=True)
