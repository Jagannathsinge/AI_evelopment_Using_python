import pyttsx3
import datetime
import speech_recognition as sr #lib for recognizing speech
import wikipedia
import webbrowser
import os
# import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("i am jayesh sir.Please tell me how may I help you")


def takeCommand():
    #it take microphone input from the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.pause_threshold = 1
        # audio = r.listen(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # query = r.recognize_google(audio ,Language = 'en-in')
        query = r.recognize_google(audio , language='en-in')
        # print(f"user said: {query}\n")
        print(f"user said : {query}\n")

    # except Exception as e:
    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query
    
if __name__ == "__main__":
    wishMe()
    takeCommand()

    while True:
    # if 1:
        query = takeCommand().lower()
        #logic for exicuting task based on query
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open college website' in query:
            webbrowser.open("mvjce.edu.in")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open chat gpt' in query:
            webbrowser.open("openai.com")

        elif 'open ipl match' in query:
            webbrowser.open("https://www.jiocinema.com/")

        # elif 'open google map' in query:
        #     webbrowser.open("www.google.co.in/maps")

        elif 'play music' in query:
            # music_dic = "D\\Non Critical\\songs\\favorite songs2"
            music_dic = "C:\\Users\\hp\\Music\\mp3 songs"
            # music_dic = "https:\\www.hungama.com\playlists\bollywood-top-40\6532\"
            songs = os.listdir(music_dic)
            print(songs)
            os.startfile(os.path.join(music_dic, songs[0]))

        elif 'the time' in query:
            startTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {startTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        
        if 'quit' in query:
            exit()