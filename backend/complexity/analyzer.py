import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "models/gemini-1.5-flash"

def analyze_complexity(code: str) -> str:
    if not code.strip():
        return "No code provided to explain."

    prompt = f"""Analyze the time and space complexity of the following code in Big O notation. 
Explain the logic and identify the dominant operations.

```python
{code}
```"""
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error from Gemini: {e}"
