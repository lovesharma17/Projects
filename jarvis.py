import speech_recognition as sr 
import webbrowser
import pyttsx3
import musiclib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(command):
    if "open google" in command.lower():
        webbrowser.open('https://google.com')
    
    elif "open youtube" in command.lower():
        webbrowser.open('https://youtube.com')

    elif command.lower().startswith('play'):
        song = command.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)


if __name__ == '__main__':

    speak('Initializing jarvis....')
    while True:

         # listen for the wake word 'jarvis'
        r = sr.Recognizer()
       
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                assert source.stream is not None  # Ensure the audio source is available
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)  # Capture audio
    # Recognize speech using Google Web Speech API
            word = r.recognize_google(audio)
            if( word.lower() == 'jarvis'):
                speak('yes master love ')

                # listen for command

                with sr.Microphone() as source:
                    assert source.stream is not None  # Ensure the audio source is available
                    print("Jarvis Active...")
                    audio = r.listen(source)  # Capture audio
                    command  = r.recognize_google(audio)

                    processcommand(command)

        
        except Exception as e:
            print("Error; {0}".format(e))

           

        


    