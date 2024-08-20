from email.message import EmailMessage
import smtplib

EMAILADDRESS = 'youremail@gmail.com'
EMAILPASS = 'XXXXXXXXXXXXX'

message = EmailMessage()
message['From'] = EMAILADDRESS
message['To'] = EMAILADDRESS
message['Subject'] = 'This is my CV'
message.set_content('You can download my cv below')


with open('yourcv.pdf', 'rb') as f:
    fdata = f.read()
    fname = f.name

message.add_attachment(fdata, maintype='application', subtype='octet-stream', filename=fname)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAILADDRESS, EMAILPASS)
    smtp.send_message(message)