import seaborn as sns
import matplotlib.pyplot as plt
import  streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("D:\Workspace\Active\Streamlit\diamonds.csv", on_bad_lines="skip")

#Add a st.selectbox() to pick a cut type. Show the selected cut
ucut = st.selectbox("Pick your CUT", df["cut"].unique())
st.success(f"you selected the {ucut} cut.")
st.divider()

#Creates a range slider. User drags to pick min/max values.
price_range = st.slider("Select Price Range", 0,20000, (0,10000))
st.success(f"Your selected range is {price_range}")
st.divider()


#Q3 — add a st.multiselect() for clarity.
mclarity = st.multiselect("Select Clarity", df["clarity"].unique())
st.write(f"you selected these {mclarity}")
st.divider()

#Q4 — combine all 3 filters together to filter the DataFrame and display it:

#st.dataframe(filtered.head(50))
st.divider()


#Q5: Add a st.radio() for color (single select). Display the selected color.
selected_color = st.radio("Select the Color", df["color"].unique())
st.success(f"Selected Color is {selected_color}")

#Q6: Add a st.number_input() for minimum carat value. Default = 0.
min_carat_value = st.number_input("Minimum Carat Value", min_value=0.0)
st.success(f"Minimum Carat Valuse is {min_carat_value}")

#Q7: Add a st.checkbox() labeled "Show only premium cuts":
check_box = st.checkbox(label="Show only premium cuts")

#Q8: Combine ALL filters into one filtered DataFrame.
filtered = df[
    (df["cut"] == ucut) &
    (df["price"].between(price_range[0],price_range[1])) &
    (df["clarity"].isin(mclarity)) &
    (df["color"] == selected_color) &
    (df["carat"] >= min_carat_value)
]
if check_box:
    filtered  = filtered[filtered["cut"] == "premium"]
st.dataframe(filtered.head(50))

with st.expander("Show Statistical Summary"):
    st.dataframe(df.describe())