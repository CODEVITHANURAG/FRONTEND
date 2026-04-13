import os
import base64
import threading
from groq import Groq
import speech_recognition as sr
import pyttsx3
from tkinter import *
from tkinter import filedialog, scrolledtext, ttk
from PIL import Image, ImageTk

# API Key
GROQ_API_KEY = ""

# System prompt for LLM

system_prompt = (
    "You are a medical assistant. Answer questions related to health, symptoms, treatments, fitness, nutrition, mental wellness, "
    "and basic medical terms or concepts. If the question isn't health-related, respond with:\n\n"
    "\"I'm here to help only with health-related questions. Please ask something related to your health or medical knowledge.\"\n\n"
    "Now my query is: "
)


# Encode image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Recognize speech using Google API
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Request error: {e}"

# Convert text to speech
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Analyze image + query using Groq API
def analyze_image_with_query(query, model, encoded_image=None):
    client = Groq(api_key=GROQ_API_KEY)
    user_content = [{"type": "text", "text": query}]
    if encoded_image:
        user_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
        })
    messages = [{"role": "user", "content": user_content}]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content

# GUI Class
class MedicalChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor HealthMate Chatbot")
        self.root.geometry("720x600")
        self.root.configure(bg="#f0f4f8")
        self.image_path = None
        self.encoded_image = None

        # Responsive layout
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(5, weight=1)

        # Title
        self.label = Label(root, text="Welcome to HealthMate", font=("Helvetica", 18, "bold"), bg="#f0f4f8")
        self.label.grid(row=0, column=0, pady=15)

        # Image display
        self.image_label = Label(root, bg="#f0f4f8")
        self.image_label.grid(row=1, column=0, pady=10)

        # Upload Button
        self.upload_button = ttk.Button(root, text="Upload Image (Optional)", command=self.upload_image)
        self.upload_button.grid(row=2, column=0, pady=5, ipadx=5)

        # Explain Button
        self.talk_button = ttk.Button(root, text="Explain your problem", command=self.process_query)
        self.talk_button.grid(row=3, column=0, pady=10, ipadx=5)

        # Output Text Area
        self.output_text = scrolledtext.ScrolledText(root, height=15, wrap=WORD, font=("Segoe UI", 11))
        self.output_text.grid(row=5, column=0, sticky="nsew", padx=20, pady=10)

    def upload_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if path:
            self.image_path = path
            self.encoded_image = encode_image(self.image_path)
            img = Image.open(self.image_path)
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img_tk)
            self.image_label.image = img_tk

    def process_query(self):
        threading.Thread(target=self._process_query_thread).start()

    def _process_query_thread(self):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", "🎤 Listening for patient's explanation...\n")
        query = recognize_speech()
        final_query = system_prompt + query
        model = "llama-3.2-90b-vision-preview"
        # model="qwen-qwq-32b"

        self.output_text.insert("end", f"\n📝 You said: {query}\n\n⏳ Processing...\n")
        response = analyze_image_with_query(final_query, model, self.encoded_image)

        self.output_text.insert("end", f"\n💬 Doctor's response:\n{response}\n")
        speak_text(response)


if __name__ == "__main__":
    root = Tk()
    app = MedicalChatbotGUI(root)
    root.mainloop()
