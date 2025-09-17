import streamlit as st
from converter import convert

st.title("Engineering Unit Conversion Tool")

value = st.number_input("Enter value", value=1.0)
from_unit = st.text_input("Enter Input UOM (e.g., ft, psi, bbl, C, F, K)")
to_unit = st.text_input("Enter Required UOM (e.g., m, Pa, m3, C, F, K)")

if st.button("Convert"):
    try:
        result = convert(value, from_unit.strip(), to_unit.strip())
        st.success(f"{value} {from_unit} = {result:.6g} {to_unit}")
    except Exception as e:
        st.error(str(e))
