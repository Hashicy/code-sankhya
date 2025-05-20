
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.explain.explainer import explain_code

st.set_page_config(page_title="Code Sankhya - AI Code Explainer", layout="wide")
st.title("🤖 Code Sankhya: AI Code Explainer")

code_input = st.text_area("Paste your code below:", height=300, placeholder="def greet():\n    print('Hello, world!')")

if st.button("Explain Code"):
    with st.spinner("Analyzing your code..."):
        explanation = explain_code(code_input)
        st.subheader("📘 Explanation:")
        st.markdown(explanation)
