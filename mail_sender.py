import smtplib

#creating server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls() #transport layer security
server.login('jakismail.prosty@gmail.com', 'Haslo123') #username and password
server.sendmail('jakismail.prosty@gmail.com',
                'jakismail.prosty@gmail.com',
                ' My message to someone')
