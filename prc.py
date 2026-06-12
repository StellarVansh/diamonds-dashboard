import streamlit as st

st.title("Hello Vansh")
st.header("Hello  cooler")
st.subheader("Hello  cooler")
st.text("Teri Ma Ki Chut")
st.write("Maa ka Bhosda AAG")
st.caption("chaal bsdk")

gaali = st.selectbox("konsi gaali deni hai", ["saale","bhnchod","chutiya","betichod"])
st.write(f"vansh {gaali}")

st.success("Aapko gaali padh chuki hai")