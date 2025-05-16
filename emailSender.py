import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

to = input("Enter the email of the recipient: ")
content = input("Enter the content for the mail:\n")

def sendmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        from_email = os.getenv('EMAIL') #Enter your gmail it should be saved in .env file 
        password = os.getenv('PASSWORD') #Email's Password which u gets from App Password in gmail

        server.login(from_email, password)
        server.sendmail(from_email, to, content)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)
    finally:
        server.quit()

sendmail(to, content)
