from email.message import EmailMessage
import smtplib

EMAILADDRESS = 'saniourry@gmail.com'
EMAILPASS = 'vmoe mboq jjae mepl'

message = EmailMessage()
message['From'] = EMAILADDRESS
message['To'] = EMAILADDRESS
message['Subject'] = 'Gumball & Darwin'
message.set_content('Say hello to Gumball and Darwin')
attachments = ['gumball.png', 'darwin.png']

with open('cv.pdf', 'rb') as f:
    fdata = f.read()
    fname = f.name

message.add_attachment(fdata, maintype='application', subtype='octet-stream', filename=fname)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAILADDRESS, EMAILPASS)
    smtp.send_message(message)