import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import logging

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Sofia Sir. Please tell me how may I help you")  

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query 

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Use environment variables or a config file to get the credentials
        server.login('khushparikh01@gmail.com', 'ogfrymscqowsexzf')
        server.sendmail('khushparikh01@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        logging.exception("Error while sending email")
        speak("Sorry my friend. I am not able to send this email")      

if __name__ == "__main__":
  wishMe()
  while True:
     query = takeCommand().lower()

     if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

     elif 'open youtube' in query:
            webbrowser.open("youtube.com")

     elif 'open google' in query:
            webbrowser.open("google.com")

     elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

     elif 'open lead code' in query:
            webbrowser.open("leetcode.com")

     elif 'play music' in query:
            music_dir ="D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

     elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kp6840@srmist.edu.in"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                logging.exception("Error while processing the email command")
                speak("Sorry my friend. I am not able to send this email")    
