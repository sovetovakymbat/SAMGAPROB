import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to generate sample data
def generate_data(n):
    return pd.DataFrame({
        'A': np.random.randn(n),
        'B': np.random.rand(n) * 100,
        'C': np.random.randint(1, 10, n)
    })

# Set up the title of the dashboard
st.title('Streamlit Example App')

# Sidebar for user inputs
st.sidebar.header('User Input Options')
data_size = st.sidebar.slider('Select the number of data points', min_value=10, max_value=1000, value=500)
chart_type = st.sidebar.selectbox('Select chart type', ['Line', 'Bar', 'Scatter'])

# Generate data
data = generate_data(data_size)

# Display data as a table
st.write("Data Preview:", data.head())

# Plotting based on the choice of chart
if chart_type == 'Line':
    st.line_chart(data)
elif chart_type == 'Bar':
    fig, ax = plt.subplots()
    data.plot(kind='bar', ax=ax)
    st.pyplot(fig)
elif chart_type == 'Scatter':
    st.write("Scatter Plot:")
    st.scatter_chart(data)

# Add a footer or additional information
st.markdown('This is a sample Streamlit app to demonstrate different types of charts using random data.')
