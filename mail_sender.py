import smtplib
import speech_recognition as sr
import pyaudio

#listener
listener = sr.Recognizer()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source=source)
            voice = listener.listen(source, )
            info = listener.recognize_google(voice, language='pl-PL', show_all=True) #en-IN
            print(info)
    except OSError:
        print('error')
#creating server
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() #transport layer security
    server.login('jakismail.prosty@gmail.com', 'Haslo123') #username and password
    server.sendmail('jakismail.prosty@gmail.com',
                   'jakismail.prosty@gmail.com',
                    ' My message to someone')
