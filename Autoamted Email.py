#This program is used to automcatically send emails

from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os

smtp = smtplib.SMTP('SMTP.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

#Enter your password and email in their respective fields
smtp.login('Your Email', 'Your Password')

msg = MIMEMultipart()
msg['Subject'] = subject
msg.attach(MIMEText(text))

to = ["Enter", "emails", "for who", "you want to send.com"]
smtp.sendmail(from_addr="Your login email",
              to_addrs=to, msg=msg.as_string())

smtp.quit()
