# VOICE-chatbot
# Voice-to-Voice Chatbot

This is a voice-to-voice chatbot built using Python, utilizing libraries such as `Tkinter`, `SpeechRecognition`, `pyttsx3`, and `google.generativeai`. The chatbot listens to user input via the microphone, processes the speech, and provides a response using text-to-speech (TTS). The assistant is powered by Google's Gemini API for generating insightful and helpful responses.

## Features
- **Speech-to-Text**: Converts spoken input into text using `SpeechRecognition`.
- **Text Generation**: Uses the `google.generativeai` API to generate responses based on user input.
- **Text-to-Speech**: Uses `pyttsx3` to read out the assistant's response.
- **Graphical User Interface (GUI)**: Built with `Tkinter` for a clean and simple interface.

## Requirements
Before running the project, make sure to install the following dependencies:
pip install tkinter speechrecognition pyttsx3 google-generativeai

## How to Use
- Press the 🎤 Speak button or say a phrase into your microphone.
- The chatbot will listen to your input, convert it to text, generate a response, and speak it back to you.
- If you want to exit the application, say "quit from the application".

## Acknowledgments
- SpeechRecognition library for converting speech to text.
- pyttsx3 for text-to-speech functionality.
- google.generativeai for generating the chatbot's responses.
- Tkinter for building the GUI.
