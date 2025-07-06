# 
Projects
🩺 SehatSathi - AI Medical Assistant
SehatSathi is a voice-enabled AI-powered medical chatbot built using Python. It allows users to speak their health concerns and optionally upload an image (e.g., of a report or rash). The assistant then responds with medically relevant guidance using a large language model (LLM) via the Groq API.

📌 Features
🎤 Voice Input — Speak your symptoms or questions directly.

🖼️ Image Upload — Attach medical images like skin issues or reports (optional).

🧠 AI Response — Powered by Groq’s large language models (LLMs) to provide reliable health advice.

🗣️ Text-to-Speech — The assistant reads the answer out loud for you.

🖼️ Tkinter GUI — Simple and clean user interface for desktop usage.

📷 Preview

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/sehatsathi-medical-chatbot.git
cd sehatsathi-medical-chatbot
2. Install dependencies
Make sure you have Python 3.10+ installed.

bash
Copy
Edit
pip install -r requirements.txt
Or install them individually:

bash
Copy
Edit
pip install speechrecognition pyttsx3 pillow groq
🔧 Note: You may also need to install pyaudio. If it fails:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
3. Set your Groq API key
Open the script and set:

python
Copy
Edit
GROQ_API_KEY = "your_groq_api_key_here"
▶️ How to Run
bash
Copy
Edit
python app.py
Then speak your question and optionally upload a medical image.

💡 Example Use Cases
Ask about cold, fever, or symptoms

Upload a rash image and ask "what might this be?"

Ask about nutrition or mental wellness

Get general medical definitions and precautions

⚠️ Disclaimer
This project is for educational/demo purposes only and not a replacement for professional medical advice. Always consult a doctor for health-related decisions.

🙌 Acknowledgements
Groq API

SpeechRecognition

Tkinter

Pillow (PIL)

Pyttsx3
