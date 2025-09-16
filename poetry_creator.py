import streamlit as st
import requests
import json
import base64

# ------------------------------
# Function to interact with Ollama (streaming enabled)
# ------------------------------
def generate_poem(words):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "gemma:2b",  # ✅ Lightweight model for 8GB RAM
        "prompt": f"Write a beautiful and creative poem using these words: {words}. "
                  f"The poem should be aesthetic, short, and engaging.",
        "stream": True
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    poem = ""
    for line in response.iter_lines():
        if line:
            json_data = json.loads(line.decode("utf-8"))
            if "response" in json_data:
                poem += json_data["response"]
    return poem.strip()

# ------------------------------
# Set background image
# ------------------------------
def set_background(png_file):
    with open(png_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.jpg")  # ✅ Replace with your image file

# ------------------------------
# Custom CSS for fonts, colors, and navbar
# ------------------------------
st.markdown("""
<style>
/* Top navigation bar */
.navbar {
    background-color: rgba(0,0,0,0.6);
    padding: 10px 30px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 30px;
}
.navbar a {
    color: #fff;
    text-decoration: none;
    font-size: 18px;
    margin: 0 20px;
    font-weight: bold;
}
.navbar a:hover {
    color: #FFD700;
}

/* Heading */
h1 {
    color: #FFD700;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    text-align: center;
}

/* Poetry text box */
.poem-box {
    background: rgba(255,255,255,0.85);
    padding: 20px;
    border-radius: 15px;
    font-size: 20px;
    color: #333;
    margin-top: 20px;
}

/* Credit text */
.credit {
    position: fixed;
    bottom: 10px;
    right: 20px;
    font-size: 14px;
    color: #fff;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Top Navigation Bar
# ------------------------------
st.markdown("""
<div class="navbar">
    <a href="#">Home</a> |
    <a href="#">About</a> |
    <a href="#">Contact</a>
</div>
""", unsafe_allow_html=True)

# ------------------------------
# App Main Content
# ------------------------------
st.title("✨ AI Poetry Creator ✨")
words = st.text_input("Enter words for your poem:", "")

if st.button("Generate Poem"):
    if words.strip() != "":
        with st.spinner("✨ Creating your poem..."):
            poem = generate_poem(words)
        st.markdown(f'<div class="poem-box">{poem}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter some words!")

# ------------------------------
# Credit
# ------------------------------
st.markdown('<div class="credit">Designed & Developed by JAY</div>', unsafe_allow_html=True)