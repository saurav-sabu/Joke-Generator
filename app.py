import streamlit as st
import pyjokes

st.title("Jokes For CS Programmer")

st.markdown("---")

_,col2,_ = st.columns(3)


with col2:
    btn = st.button("Click Me")


if btn:
    st.markdown(f"> {pyjokes.get_joke()}")