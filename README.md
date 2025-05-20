# 🧠 Code Sankhya

Code Sankhya is an AI-powered code explainer that breaks down code line-by-line in plain English. Designed especially for CP (Competitive Programming) learners, it helps users understand complex logic and structure effortlessly.

---

## 🚀 Features

- ✨ **Line-by-line Code Explanation**
- 🧮 **Complexity Analysis** (coming soon)
- 🐞 **Bug Finder & Fix Suggestions** (coming soon)
- 📊 **Flowchart Generator** (coming soon)
- 🔁 Supports **Python**, **C/C++**, **Java**, and more (planned)

---

## 🛠 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend AI:** [Google Gemini API](https://ai.google.dev/)
- **Environment Management:** `venv`, `.env`
- **Language Support:** Python 3.12+

---

## 🔧 Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/code-sankhya.git
cd code-sankhya

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add your Gemini API key
echo "GEMINI_API_KEY=your-key-here" > .env

# 5. Run the app
streamlit run app/main.py
