import speech_recognition as sr  # Importing Module

r = sr.Recognizer()  # Importing recognizer class and initializing an instance of it to r


def myCommand():  # Function to convert audio to text
    with sr.Microphone() as source:  # Creating Microphone Object
      print("Say something!")
      audio = r.listen(source)  # Listening to the audio

      try:  # Try to convert audio to text
        
        query = r.recognize_google(audio, language='en-in') # Converting audio to text
        print("You said " + query)

      except sr.UnknownValueError:  # Error handling
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query  # Returning the text

while True:
   myCommand()
      
