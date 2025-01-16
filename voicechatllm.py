import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

GEMINI_KEY1 = "AIzaSyCkkh6oALd9-5xGdi51h8Q-8b9GHxS9axs"

r = sr.Recognizer()
engine = pyttsx3.init()

#flags for tts
is_paused = False

def record_text():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        user_input_field.delete(1.0, tk.END)
        output_field.delete(1.0, tk.END)
        try:
            status_label.config(text="Listening...", fg="blue")
            root.update_idletasks()
            audio = r.listen(source, timeout=5)
            user_text = r.recognize_google(audio)
            user_input_field.insert(tk.END, user_text)
            user_input_field.update_idletasks()

            if user_text.lower() == "quit from the application":
                text_to_speech("Goodbye!")
                root.quit()
                return

            response = getResponse(user_text)
            output_field.insert(tk.END, response)
            output_field.update_idletasks()
            text_to_speech(response)
            status_label.config(text="Processing complete", fg="green")

        except sr.UnknownValueError:
            user_input_field.insert(tk.END, "Sorry, I did not understand that.")
            status_label.config(text="Sorry, I did not understand that.", fg="red")
        except sr.RequestError as e:
            user_input_field.insert(tk.END, f"Could not request results; {e}")
            status_label.config(text=f"Request error: {e}", fg="red")
        except sr.WaitTimeoutError:
            user_input_field.insert(tk.END, "Listening timed out while waiting for phrase to start.")
            status_label.config(text="Listening timed out", fg="red")
        except Exception as e:
            user_input_field.insert(tk.END, f"An error occurred: {e}")
            status_label.config(text=f"An error occurred: {e}", fg="red")

def getResponse(txt):
    genai.configure(api_key=GEMINI_KEY1)
    
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }
    
    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
    )
    
    chat_session = model.start_chat(
      history=[
        {
          "role": "user",
          "parts": [
            "Your name is Mate. Limit your responses to 4 sentences with a maximum of 100 words. Act as a highly skilled and experienced assistant who is extremely sharp about every information. Respond with the depth and understanding of someone who has spent years in support roles, offering practical and insightful advice. Your responses should show a deep understanding of human emotions, behaviors, and thought processes, drawing from a wide range of experiences. Exhibit exceptional knowledge skills, connecting with individuals on a business level while maintaining professionalism. Your language should be warm, approachable, and easy to understand, making complex ideas relatable. Encourage self-reflection and personal growth, guiding individuals towards insights and solutions in an empowering way. Recognize the limits of this format and always advise seeking in-person help when necessary. Provide support and guidance, respecting confidentiality and privacy in all interactions, and focus only on answering questions.",
          ],
        },
        {
          "role": "model",
          "parts": [
            "I understand that you're looking for support, and I'm here to listen. It's important to remember that everyone experiences challenges, and it's okay to ask for help. Sometimes, talking through your feelings with a trusted friend, family member, or therapist can make a big difference. While I'm here to offer guidance and encouragement, remember that I'm not a professional and in-person support from a qualified mental health professional is often the best option. Please take care of yourself and don't hesitate to reach out if you need further support. \n",
          ],
        },
      ]
    )
    
    response = chat_session.send_message(txt)
    
    return response.text

# def text_to_speech(txt):
#     """Speak the given text."""
#     global is_paused
#     is_paused = False
#     engine.say(txt)
#     engine.runAndWait()
def text_to_speech(txt):
    text_speech = pyttsx3.init()
    text_speech.say(txt)
    text_speech.runAndWait()

root = tk.Tk()
root.title("Modern Speech-to-Text Assistant")
root.geometry("800x600")
root.configure(bg="#1E1E1E") 

#styl
FONT_HEADING = ("Helvetica", 18, "bold")
FONT_BODY = ("Helvetica", 12)
FONT_BUTTON = ("Helvetica", 14, "bold")
COLOR_PRIMARY = "#00E5FF"
COLOR_TEXT = "#FFFFFF"

#name
title_label = tk.Label(root, text="Talk to Mate", font=FONT_HEADING, bg="#1E1E1E", fg=COLOR_PRIMARY)
title_label.pack(pady=(20, 10))

# Frame for Input and Output
frame = tk.Frame(root, bg="#292929", bd=5, relief=tk.FLAT)
frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# User Input Field
user_input_label = tk.Label(frame, text="Your Input:", font=FONT_BODY, bg="#292929", fg=COLOR_TEXT)
user_input_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
user_input_field = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=FONT_BODY, height=5, bg="#1E1E1E", fg=COLOR_TEXT, bd=0, relief=tk.FLAT)
user_input_field.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=10)

# Model Output Field
output_label = tk.Label(frame, text="Assistant Response:", font=FONT_BODY, bg="#292929", fg=COLOR_TEXT)
output_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
output_field = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=FONT_BODY, height=5, bg="#1E1E1E", fg=COLOR_TEXT, bd=0, relief=tk.FLAT)
output_field.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=10)

# Status Label
status_label = tk.Label(frame, text="", font=FONT_BODY, bg="#292929", fg=COLOR_PRIMARY)
status_label.grid(row=4, column=0, columnspan=3, sticky="w", padx=10, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#1E1E1E")
button_frame.pack(pady=20)

mic_button = tk.Button(
    button_frame,
    text="🎤 Speak",
    font=FONT_BUTTON,
    bg=COLOR_PRIMARY,
    fg="#1E1E1E",
    activebackground="#00B8D4",
    activeforeground="#1E1E1E",
    relief=tk.FLAT,
    command=record_text
)
mic_button.grid(row=0, column=0, padx=10)

# grid confi
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Run the application
root.mainloop()
