#!/usr/bin/python

# This script creates an HTML email and sends through Gmail

import smtplib

import csv

from bs4 import BeautifulSoup

from time import sleep

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = raw_input('Enter username: ')  # asking for username for Gmail server
password = raw_input('Enter password: ')  # password for Gmail account (app password)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)  # Setting smtp object with smtp server

smtpObj.ehlo()  # Say hello to server

smtpObj.starttls()  # TLS Encryption

smtpObj.login(username, password) # Login to SMTP server

HEADERS = ['Name', 'Email', 'Company'] # Header row for csv file

# opens csv file and reads each row
with open('emails.csv', 'rU') as csvfile:
    reader = csv.DictReader(csvfile, HEADERS)
    # reading each row
    for row in reader:

        if not row['Name'] or not row['Email'] or not row['Company']:
            continue

        soup = BeautifulSoup(open("content.html"), 'html.parser')  # parses HTML file and creates soup obj

        message = MIMEMultipart('alternative')  # creates message

        message['Subject'] = "A couple quick questions"  # message subject line

        html = str(soup)  # soup obj into string

        content = html.format(**row)

        email = MIMEText(content, 'html')  # creates email

        message.attach(email)  # combines email and message components

        recipient = row['Email']  # Sets email address for recipient

        smtpObj.sendmail(username, recipient, message.as_string())  # Sending email

        print(recipient)  # Prints each recipient to the console

        sleep(3)  # Time delay in seconds after each iteration

smtpObj.quit()  # Disconnect from server
