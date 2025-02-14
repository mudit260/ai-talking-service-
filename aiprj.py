import speech_recognition as sr
import pyttsx3
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hey there! How can I help?"]
    ],
    [
        r"what is your name?",
        ["I am a voice-activated chatbot.", "You can call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thanks for asking!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care."]
    ]
]

chatbot = Chat(pairs, reflections)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Could not request results. Check your internet connection."

def voice_chatbot():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break
        response = chatbot.respond(command)
        if response:
            print("Bot:", response)
            speak(response)
        else:
            speak("I'm not sure how to respond to that.")

if __name__ == "__main__":
    voice_chatbot()
