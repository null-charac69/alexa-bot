import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            # talk(command)

    except:
        command = r'I couldn"t understand your command'
    return command 

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        song = song.replace('alexa', '').strip()
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'wikipedia' in command or 'who is' in command or 'what is' in command or 'tell me about' in command or 'who the heck is' in command:
        person = command.replace('wikipedia', '').replace('who is', '').replace('what is', '').replace('tell me about', '').replace('who the heck is', '')
        info = wikipedia.summary(person, 3)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')

run_alexa() 