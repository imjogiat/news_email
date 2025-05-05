import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage


def send_email(message):    
    #Step 1: Set the host string and port number integer
    host = "smtp.gmail.com"
    port = 465

    #Step 2: Get an App password from gmail
    
    #Step 3: Set the sending email(username) and password of that account
    #  and set the receiver email

    #PASSWORD env variable is not authenticating, only string password variable 
    #authenticates and sends email- not obvious why currently
    #will leave as string password for now while testing
    #**REMOVE STRING PASSWORD BEFORE COMMITING AND PUSHING TO GITHUB**
    username = "org.imj.yyc@gmail.com"
    password = "PASSWORD"
    # password = os.getenv("PASSWORD")

    receive_email = "imjogiat@gmail.com"

    #Step 4: define a secure SSL context
    context = ssl.create_default_context()


    #Step 5: call SMTP_SSL method from smtplib library with parameters shown. 
    # This creates a mail server object that can
    #log in to an email address, send emails and other object methods based on 
    # method parameters when called

    with smtplib.SMTP_SSL(host, port, context=context) as mailserver:
        mailserver.login(username, password)
        mailserver.send_message(message, username, receive_email)
       