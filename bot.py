import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)
newvoicerate=110
engine.setProperty('rate',newvoicerate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            talk('listening...')
            voice=listener.listen(source)
            text=listener.recognize_google(voice)
            text=text.lower()
            if 'mayur' in text:
                text=text.replace('mayur','')           
    except:
        print('MICROPHONE ERROR...')
        talk('MICROPHONE ERROR...')
        pass
    return text

def run_bot():
    text=talk_command()
    print(text)
    if 'play' in text:
        song=text.replace('play','')
        talk('Playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in text:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' +time)
    elif 'about' in text:
        information=text.replace('about','')
        info=wikipedia.summary(information)
        print(info)
        talk(info)
    elif 'joke' in text:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
        
    else:
        talk('Please repeat again...')
      
talk('I am Your ObedientBot')
talk('What can I do for You?...Boss!')
while True:
    run_bot() 
   
       
    