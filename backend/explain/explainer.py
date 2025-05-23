
import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "models/gemini-1.5-flash"

def explain_code(code: str) -> str:
    if not code.strip():
        return "No code provided to explain."

    prompt = f"Explain the following code line by line in simple English:\n\n{code}"

    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error from Gemini: {e}"
