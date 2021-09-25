import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M")  
   
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")   

    else:
        speak("Good Evening Sir")  

    speak("The Time is") 
    speak(strTime)
    speak("I am Friday.")     


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("How may i help you Sir")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        speak("1 Moment Sir")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        print("Say that again please...")  
        return "None"
    return query

#def sendEmail(to, content):
#   server = smtplib.SMTP('smtp.gmail.com', 587)
#   server.ehlo()
#   server.starttls()
#   server.login('youremail@gmail.com', 'your-password')
#   server.sendmail('youremail@gmail.com', to, content)
#   server.close()

if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'friday open youtube' in query:
            webbrowser.open("youtube.com")
            speak("As you wish Sir")

        elif 'friday hello' in query:
            speak("hello Sir,how are you")

        elif 'friday how are you' in query:
            speak("i am fine sir ,how are you")

        elif 'friday i miss you' in query:
            speak("Same Here Sir...")
            webbrowser.open("https://www.youtube.com/watch?v=qdpXxGPqW-Y")

        elif 'friday open google' in query:
            webbrowser.open("google.com")
            speak("As you wish Sir")

        elif 'friday open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            speak("As you wish Sir")

        elif 'friday play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=HPkydJOXXNs")
            speak("As you wish Sir , if you want me to play english song then tell friday play english song")

        elif 'friday play english song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=lzylyTyca8A")
            speak("As you wish Sir")

        elif 'friday the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'friday i want to draw' in query:
            webbrowser.open("https://i.pinimg.com/originals/d5/1f/e8/d51fe80ddac667a928d8e4b87d7cf949.jpg")
            speak("As you wish Sir")

        elif 'friday open code' in query:
            codePath = "C:\\Users\\akcod\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
            speak("As you wish Sir")

        elif 'friday open roblox' in query:
            codePath = "C:\\Users\\akcod\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
            speak("As you wish Sir")

        elif 'friday shutdown' in query:
            speak("Thank you Sir")

        elif 'friday i want to dance' in query:
            webbrowser.open("https://www.youtube.com/watch?v=n1oaPb_UTxs")
            speak("As you wish Sir")

        #elif 'play music' in query:
           # music_dir = 'C:\\Users\\akcod\\OneDrive\\Pictures\\Music'
           # songs = os.listdir(music_dir)
           # print(songs)    
           # os.startfile(os.path.join(music_dir, songs[5]))

        #elif 'friday email to aditya' in query:
        #    try:
        #       speak("What should I say?")
        #      content = takeCommand()
        #      to = "adityayourEmail@gmail.com"    
        #     sendEmail(to, content)
        #     speak("Email has been sent!")
        # except Exception as e:
        #     print(e)
        #    speak("Sorry my friend harry bhai. I am not able to send this email")    