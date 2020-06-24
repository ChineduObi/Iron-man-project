import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")
MASTER = "Mister Chinneedu"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#speak funcition will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish you as per the current time
def wishMe():
    hour = datetime.datetime.now().hour
    print(hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("I am Jarvis. How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
        # query = r.recognize_google(audio)

    except Exception as e:
        print("Say that again please")
        query = None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("chineduobi423@gmail.com", "Chineduobi321")
    server.sendmail("nafi.roza@gmail.com", to, content)
    server.close()

#Main Program starts here...



speak("Initialising Jarvis...")
wishMe()



#Logic for executing task as per the query
while True:
    query = takeCommand()
    if "exit" in query.lower() or "thank you" in query.lower():
        break

    if "wikipedia" in query.lower():
            speak("searching wikipedia...")
            query = query.replace("according to wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

    elif "open youtube" in query.lower():
        webbrowser.open("youtube.com")

    elif "open google" in query.lower():
        webbrowser.open("google.com")

    elif "play music" in query.lower():
        songs_dir = ("c:\\Users\\owner\\Music\\colors\\Masego\\Lady Lady")
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "the time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'{MASTER} the time is {strTime}')

    elif "open code" in query.lower():
        codePath = "C:\\Users\\owner\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif "email to someone" in query.lower():
        try: 
            speak("What should I send")
            content = takeCommand()
            to = "nafi.roza@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
            print(e)
    



# if query.lower() != "exit" or query.lower() != "Thank you":
#     takeCommand()

# else:
#     exit()