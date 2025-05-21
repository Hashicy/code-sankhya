
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from backend.explain.explainer import explain_code
from backend.complexity.analyzer import analyze_complexity
from backend.explain.patterns import detect_patterns

st.set_page_config(page_title="Code Sankhya - AI Code Explainer", layout="wide")
st.title("🤖 Code Sankhya: AI Code Explainer")

code_input = st.text_area("Paste your code below:", height=300, placeholder="def greet():\n    print('Hello, world!')")

if st.button("Explain Code"):
    with st.spinner("Analyzing your code..."):
        explanation = explain_code(code_input)
        complexity = analyze_complexity(code_input)
        patterns = detect_patterns(code_input)

        st.subheader("📘 Explanation:")
        st.markdown(explanation)


        st.subheader("⏱️ Time & Space Complexity:")
        st.write(complexity)

        st.subheader("♟️ Detected CP Patterns:")
        if patterns:
            st.markdown(", ".join(patterns))
        else:
            st.markdown("No common CP pattern detected.")

