✨ AI Poetry Creator  

An interactive **AI-powered poetry generator** built with **Streamlit** and **Ollama’s Gemma:2B model**.  
Create unique poems instantly, switch between light/dark themes, and download your creations in `.txt` or `.pdf` format.  

![App Screenshot](screenshot.png) <!-- optional: add your screenshot -->



🚀 Features  
- 🎨 **Dark/Light Mode Toggle** – choose your preferred theme.  
- 📝 **AI Poem Generator** – powered by **Gemma:2B** running locally via Ollama.  
- 💾 **Download Poems** – save poems as `.txt` or `.pdf`.  
- 🖼️ **Custom Background** – add your own creative flair.  
- ⚡ **Lightweight & Fast** – optimized for **8GB RAM laptops**.  



📦 Installation  

1. Clone the repository  
```bash
git clone https://github.com/your-username/ai-poetry-creator.git
cd ai-poetry-creator
pip install -r requirements.txt
ollama pull gemma:2b
streamlit run app.py


🛠 Requirements
pip install -r requirements.txt
streamlit
requests
reportlab


Stucture*
📦 ai-poetry-creator
 ┣ 📜 app.py              # Main Streamlit app
 ┣ 📜 requirements.txt    # Python dependencies
 ┣ 📜 README.md           # Project documentation
 ┣ 📜 background.jpg      # (Optional) Background image
 ┗ 📜 .gitignore

