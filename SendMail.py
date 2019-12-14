import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Constants import *
from Utils import *

def sendEmail ():
    # Send the message via local SMTP server.
    mail = smtplib.SMTP(PROTOCOL, PORT)
    mail.ehlo()
    mail.starttls()
    mail.login(SENDER, PASSWORD)

    for RECEIVER in list(SAMPLE_PAYLOAD.keys()):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = SUBJECT
        msg['From'] = SENDER
        new_html = replaceHtml(RECEIVER, SAMPLE_HTML)
        html_content = MIMEText(new_html, 'html')
        msg.attach(html_content)
        msg['To'] = RECEIVER
        try:
            mail.sendmail(SENDER, RECEIVER, msg.as_string())
            print("\nMail sent to "+ RECEIVER)
        except:
            print ("An error occured.")
    mail.quit()
