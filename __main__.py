import os
import pandas as pd
import sys
from datetime import datetime as dt, timedelta as td
import time

sender_email = os.environ.get('SENDER_EMAIL')
sender_password = os.environ.get('SENDER_EMAIL_PASSWORD')

def send_mail(mail_details):
    print('Sending Mail to '+mail_details)

def get_mailing_list(filename):
    if filename.endswith('csv'):
        df = pd.read_csv(filename)
        return df

def main(args=None):

    mail_list = get_mailing_list(sys.argv[1])

    for mail in mail_list.email.to_list():
        send_mail(mail)
        time.sleep(1)

if __name__=='__main__':
    main()
