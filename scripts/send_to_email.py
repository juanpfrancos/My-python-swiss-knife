import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(file_, receiver_email):
    try:
        now = datetime.now().isoformat()
        sender_email = os.environ["SENDER_EMAIL"]
        password_app = os.environ["PWD_APP"]
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"Informe Covid {now}"
        body = f"Hola, adjunto el archivo de excel {now}"
        message.attach(MIMEText(body, "plain"))
        attach = MIMEApplication(file_, _subtype = "xlsx")
        attach.add_header("Content-Disposition", "attachment", filename = f"archivo{now.replace(':','')}.xlsx")
        message.attach(attach)
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, password_app)
            smtp.send_message(message)
    except Exception as e:
        raise ValueError("Error sending email") 