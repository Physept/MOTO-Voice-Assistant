import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import random
import os
import psutil
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
engine.setProperty('volume', 50)

def speak(text):
    engine.say(text)
    engine.runAndWait()
##
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
            return ""

        except sr.RequestError:
            speak("I am having trouble connecting to the speech recognition service.")
            return ""
        return command
##
def load_name() -> str:
    """Loads the assistant's name from a file, or uses a default name."""
    try:
        with open("assistant_name.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "MOTO"  # Default name
##
def wishme() -> None:
    speak("Welcome back, sudeep!")
    print("Welcome back, sudeep!")
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning!")
        print("Good morning!")
    elif 12 <= hour < 16:
        speak("Good afternoon!")
        print("Good afternoon!")
    elif 16 <= hour < 24:
        speak("Good evening!")
        print("Good evening!")
    else:
        speak("Good night,it's beging late,take rest boss")
    assistant_name = load_name()
    speak(f"{assistant_name} at your service.")
    print(f"{assistant_name} at your service.")
##
def buddy():
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good morning, Have you completed your breakfast!")
        print("Good morning, Have you completed your breakfast!")
    elif 12 <= hour < 16:
        speak("Good afternoon! Boss did you complete yor lunch")
        print("Good afternoon! Boss did you complete yor lunch")
    elif 16 <= hour < 24:
        speak("Good evening! It's a great time to go for a walk.")
        print("Good evening! It's a great time to go for a walk.")
    else:
        speak("Good night,it's being late,take rest boss")
##
def play_music():
    music_folder = r"C:\Users\Siddhartha\Downloads\Music"
    try:
        files = [f for f in os.listdir(music_folder) if os.path.isfile(os.path.join(music_folder, f))]
        if not files:
            speak("No music files found in the folder.")
            return
        file_path = os.path.join(music_folder, random.choice(files))
        os.startfile(file_path)
    except Exception as e:
        speak(f"An error occurred: {e}")
##
def stop_music():
    try:
        subprocess.call(["taskkill", "/IM", "wmplayer.exe", "/F"])
    except Exception as e:
        speak(f"An error occurred while stopping the music: {e}")
##
def get_weather():
    while True:
        city="Durgapur"
        speak("Which city's weather would you like to know?")
        city = listen()
        api_key = "14ffe4ad8032d676741ec694d2970e04"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            weather_data = response.json()
            if weather_data.get("cod") != 200:
                speak(f"Could not fetch weather data for {city}.")
            else:
                temp = weather_data["main"]["temp"]
                weather_desc = weather_data["weather"][0]["description"]
                speak(f"The current temperature in {city} is {temp}°C with {weather_desc}.")
                print(f"The current temperature in {city} is {temp}°C with {weather_desc}.")
                break
        except Exception as e:
            speak(f"An error occurred while fetching weather: {e}")

        if "done" in city:
            return
##
def open_ppt():

    ppt_file = "C:/Users/Siddhartha/Downloads/sudip final project/Sudip final ppt.pptx"
    if os.path.exists(ppt_file):
        print(f"Opening PowerPoint file: {ppt_file}")
        subprocess.Popen([ppt_file], shell=True)
    else:
        print("The specified PowerPoint file does not exist.")
##
def system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    speak(f"CPU usage is at {cpu_percent} percent.")
    speak(f"Available memory is {memory_info.available // (1024 * 1024)} megabytes.")
##
def handle_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        buddy()
    ##
    elif "powerpoint" in command:
        # Call the function
        open_ppt()
    ##
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}.")
        speak("today is very important day for us, so best of luck for our project presentation ")
    ##
    elif "thank" in command:
        speak("welcome boss,so nice of you!")
    ##
    elif "open this pc" in command:
        os.system("explorer shell:MyComputerFolder")
        speak("Opening This PC")
    ##
    elif "play music" in command:
        play_music()
        speak("Playing music from your device.")
    ##
    elif "stop music" in command:
        stop_music()
        speak("Music stopped.")
    ##
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    ##
    elif "about yourself" in command:
        speak("Hello, my name is Moto, your assistant.")
    ##
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    ##
    elif "search google" in command:
        search_query = command.replace("search google for", "").strip()
        if search_query:
            encoded_query = urllib.parse.quote_plus(search_query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open(search_url)
            speak(f"Searching Google for {search_query}")
        else:
            speak("I couldn't understand the search query.")
    ##
    elif "weather" in command:
        get_weather()
    ##
    elif "system information" in command:
        system_info()
    ##
    elif "see you tomorrow" or "good night" or "bye" in command:
        speak("radhae radhae,........,take care boss!")
        return False
    ##
    else:
        speak("I am not sure how to help with that.")
    return True


def main():
    speak("Please tell me how may I assist you")
    while True:
        command = listen()
        if command:
            if not handle_command(command):
                return

if __name__ == "__main__":
    wishme()
    main()



