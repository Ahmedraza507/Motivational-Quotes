import smtplib
import pandas as pd
from datetime import datetime

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "muhammadahmedraza987@gmail.com"
GMAIL_PASSWORD = "akls wjzw ivcl dztf"

def send_email(email, subject, motivationalquote):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
             server.starttls()
             server.login(GMAIL_USER, GMAIL_PASSWORD)
             email_message = f"Subject: {subject}\n\n*** {motivationalquote} ***"
             server.sendmail(GMAIL_USER, email, email_message)

        print(f"Successfully sent email to {email}")

    except Exception as e:
        print(f"Failed to send email to {email} : {e}")

def check_day():
    date = datetime.now()
    day = date.strftime("%A")

    if day == "Monday":

        emails = pd.read_csv("emails.csv")
        quotes = pd.read_csv("Quotes.csv")

        motivationalquotes = random.choice(quotes['quotes'])

        for index, row in emails.iterrows():
            email = row["email"]

        subject = "***is hafte ki motivational shayri***"
        message = f"Hi {name},\nyeh hey apke lia is hafte ki shayri ->\n{quote}"
        send_email(email, subject, motivationalquote)

    else :
        print(f"Sorry Today {day} Emails is only send on monday")

if __name__ == "__main__":
    check_day()