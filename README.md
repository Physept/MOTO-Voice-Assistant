# Voice Assistant

A simple Python-based voice assistant that listens to your commands and performs various tasks like searching the web, opening websites, and responding with text-to-speech.

## Features
- Recognizes voice commands
- Responds with text-to-speech
- Opens websites in a browser
- Retrieves current date and time

## Requirements
Before running the program, ensure you have installed the required dependencies in a virtual environment.

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Physept/MOTO-Voice-Assistant
   cd MOTO-voice-assistant
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program:**
   ```bash
   python voice_assistant.py
   ```

## Dependencies
- `SpeechRecognition`
- `pyttsx3`
- `webbrowser`
- `datetime`

Make sure all required libraries are installed before running the script.

## License
This project is licensed under the MIT License.

