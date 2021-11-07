import os
import pandas as pd
import sys
from datetime import datetime as dt, timedelta as td
import time
import smtplib
import ssl

sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_EMAIL_PASSWORD')
smtp_server = "smtp.gmail.com"
port = 587

context = ssl.create_default_context()
server = smtplib.SMTP(smtp_server,port)
server.starttls(context=context)
server.login(sender_email, sender_password)

def send_mail(receiver_email, message='Test Message'):

    print('Sending Mail to '+mail_details)
    server.sendmail(sender_email, receiver_email, message)

def get_mailing_list(filename):
    if filename.endswith('csv'):
        df = pd.read_csv(filename)
        return df

def main(args=None):

    global server

    mail_list = get_mailing_list(sys.argv[1])

    for mail in mail_list.email.to_list():
        send_mail(mail)
        time.sleep(1)
    server.quit()

if __name__=='__main__':
    main()
