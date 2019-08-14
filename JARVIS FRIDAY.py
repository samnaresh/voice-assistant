import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 3].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetme():
    currenth = int(datetime.datetime.now().hour)
    if currenth >= 0 and currenth < 12:
        speak('Good Morning!')

    if currenth >= 12 and currenth < 18:
        speak('Good Afternoon!')

    if currenth >= 18 and currenth != 0:
        speak('Good Evening!')


greetme()

speak('Hello Sam, I am JARVIS!')
speak('How may I help you?')


def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sam! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = mycommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = mycommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = mycommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sam! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sam')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sam')

        elif 'bye' in query:
            speak('Bye Sam.')
            sys.exit()

        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')

        speak('Next Command! Sam!')