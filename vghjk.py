import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio), "\n")
    except:
        pass
