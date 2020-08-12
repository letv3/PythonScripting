import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Oleksandr Lytvyn'
email['to'] = 'letvyk99@gmail.com'
email['sunject'] = 'you won 100 bucks'

email.set_content(html.substitute(name='Oleh Bilykh'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kemtasistent@gmail.com', 'KEMT-asis')
    smtp.send_message(email)
    print("all good")

