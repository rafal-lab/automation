import smtplib
import speech_recognition as sr
import pyaudio
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer() #listening engine
engine  = pyttsx3.init() #declaring speking engine

def talk(text):
    #application is talking text
    engine.say(text)
    engine.runAndWait()

def get_info():
    #getting info about mail contents
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source=source)
            voice = listener.listen(source, )
            info = listener.recognize_google(voice) #en-IN
            print(info)
            return info.lower()
    except OSError:
        print('error')
#creating server

def send_email(receiver, topic, content):
    #sending mail form selecting emeail to the second one
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #transport layer security
    server.login('jakismail.prosty@gmail.com', 'Haslo123') #username and password
    email = EmailMessage()
    email['From'] = 'jakismail.prosty@gmail.com'
    email['To'] = receiver
    email['Subject'] = topic
    email.set_content(content)
    server.send_message(email)

email_list = { #dictionary of name connected with email
    'some' : 'jakismail.prosty@gmail.com',
}



def get_email_info():
    while 1:
        talk('To whoam you want to send email? ')
        name = get_info()
        receiver = email_list[name]
        talk('Jaki jest temat wiadomosc?')
        topic = get_info()
        talk('Jaka jest tresc maila?')
        content = get_info()
        send_email(receiver, topic, content)
        talk('Email was succesfully send')
        talk('Do you want to send more email?')
        send_more =get_info()
        if 'no' in send_more:
            break


get_email_info()
