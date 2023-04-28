import speech_recognition as sr # Importing Module as sr

r = sr.Recognizer() # Importing recognizer class and initializing an instance

def myCommand():
    with sr.Microphone() as source:
        print("say Something")
        audio=r.listen(source)

        try :
          query = r.recognize_google(audio,language='en-in')
          print("You Said : "+query)

        except sr.UnknownValueError:
            print("Sorry sir I didn't get that")
    return query

while True:
    myCommand()
