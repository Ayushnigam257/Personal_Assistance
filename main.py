import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[1].id)
print(voices[1])
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('good morning')
    elif hour > 12 and hour < 16:
        speak('good after noon')
    else:
        speak('good evening')
    speak("hello sir i am your asssistant how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("recognising............")
        query= r.recognize_google(audio,language='eng-in')
        print('user said.....',query)
    except Exception as e:
        print(e)
        print("Say Agaain")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youra2gmail.com','password')
    server.sendmail('youemail@gmail', to ,content)
    server.close()


if __name__ == '__main__':

    wishMe()
    query=takeCommand().lower()
    speak("please wait searching")
    if "wikipedia" in query:
        query=query.replace("wikipedia"," ")
        results=wikipedia.summary(query,sentences=2)
        speak("according to wekipedia")
        speak(results)
    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open wekipedia" in query:
        webbrowser.open("wikipedia.com")
    elif "open stackoverflow" in query:
        webbrowser.open("stackoverflow.com")
    elif "play music" in query:
        music_dir="F:\\hollywood movies"
        songs= os.listdir(music_dir)
        print(songs)
    elif "the time" in query:
        strTime= datetime.datetime.now().strftime("%H,%M,%S")
        speak(f"sir the time is {strTime}")
    elif "open pycharm" in query:
        codepath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.2\\bin\\pycharm64.exe"
        os.startfile(codepath)
    elif "youtube" in query:
        query=query.replace("youtube"," ")
        speak('playing' + query)
        pywhatkit.playonyt(query)
    elif "joke" in query:
        speak(pyjokes.get_joke())
    elif "email to user" in query:
        try:
            speak("what should i say")
            content = takeCommand()
            to="useryour@gmail.com"
            sendEmail(to,content)
            speak("email has been sent")
        except Exception as e:
            print(e)
            speak("i am not able to send messages")