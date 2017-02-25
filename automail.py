#!/usr/bin/python

# This script creates an HTML email and sends through Gmail

import smtplib

import csv

from bs4 import BeautifulSoup

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

username = raw_input('Enter username: ')  # asking for username for gmail server
password = raw_input('Enter password: ')  # password for gmail account (app password)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)  # Setting smtp object with smtp server

smtpObj.ehlo()  # Say hello to server

smtpObj.starttls()  # TLS Encryption

smtpObj.login(username, password) # Login to SMTP server

# opens csv file and reads each row
with open('emails.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # reading each row
    for row in reader:
        l = row[0].split(',')  # each row is read as one list item, splits into multiple list items delimited by comma

        name = l[0]  # sets name from first list item

        recipient = l[1]  # sets email address from second list item

        soup = BeautifulSoup(open("content.html"), 'html.parser')  # parses HTML file and creates soup obj

        message = MIMEMultipart('alternative')  # creates message

        message['Subject'] = "Test"  # message subject line

        content = str(soup).format(name)  # soup obj into string

        email = MIMEText(content, 'html')  # creates email

        message.attach(email)  # combines email and message components

        smtpObj.sendmail(username, recipient, message.as_string())  # Sending email

smtpObj.quit()  # Disconnect from server








