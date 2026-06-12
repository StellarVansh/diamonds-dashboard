import seaborn as sns
import matplotlib.pyplot as plt
import  streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("D:\Workspace\Active\Streamlit\diamonds.csv", on_bad_lines="skip")

#Display a title: "Diamonds Dashboard"
st.title("Diamond Dashboard")

#Load the diamonds dataset and display the first 10 rows using st.dataframe()
st.dataframe(data= df.head(10))

#Q3: Show the column names using st.write().
st.write(df.columns.to_list())

#Q4: Show basic stats with a header:
st.write("#Stats")
st.write(df.describe())