
import requests
import smtplib
from email.mime.text import MIMEText

def send_slack_notification(webhook_url, message):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Notifica Slack inviata con successo.")
    else:
        print(f"Errore Slack: {response.status_code}")

def send_email_notification(smtp_server, port, sender_email, recipient_email, password, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("Email inviata con successo.")
