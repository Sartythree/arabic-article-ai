import streamlit as st
import openai
import docx2txt
from PyPDF2 import PdfReader
import tempfile
import os

# --- CONFIG ---
st.set_page_config(page_title="Arabic Article AI Optimizer", layout="wide")
API_KEY = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else st.text_input("Enter your OpenAI API key:", "", type="password")

# --- UTILITIES ---
@st.cache_data
def read_article(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            reader = PdfReader(tmp.name)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
        os.unlink(tmp.name)
        return "\n".join(text)
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(file.read())
            text = docx2txt.process(tmp.name)
        os.unlink(tmp.name)
        return text
    else:
        return None

def gpt(prompt, max_tokens=1300, temp=0.8):
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}],
        temperature=temp,
        max_tokens=max_tokens,
        n=1,
    )
    return response["choices"][0]["message"]["content"]

# --- PROMPTS ---
def make_seo_prompt(article):
    return f'''
🎯 **Objective**:
Transform the following Arabic article into a highly readable, SEO-optimized, and engaging piece.

📝 **Tone & Format Requirements**:
- Language: Arabic (Fusha, journalistic but clear and simple)
- Structure:
  - SEO-friendly title
  - Intro paragraph with search-intent trigger
  - Use H2 and H3 headings
  - Numbered or bulleted lists if needed
  - Embedded YouTube links as clickable calls to action
  - Conclusion with a question to encourage engagement
- Add a keywords section at the end

🧠 **Content Strategy**:
- Highlight main names, trends, or moments
- Add subheadings for each main story or artist to improve SEO
- Make each section scannable and informative
- Use bold statements, data points, or time markers to increase authority

🔍 **SEO Optimization Instructions**:
- Add relevant keywords naturally in titles and throughout the article
- Use strong opening hook to match trending search intent
- Optimize for voice search and snippets by using questions or listicles

🛠 **DO NOT**: Do not translate, summarize, or remove core content.

📄 **Source Article**:
