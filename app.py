import streamlit as st
st.title("moeto purvo prilozenie")
name=st.text_input("Kak se kazvash")
if name :
  st.write(f"Zdravei, {name}!"")
