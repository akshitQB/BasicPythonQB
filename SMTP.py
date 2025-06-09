
import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, sender_email, password, receiver_email):
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email

    def send_email(self):
        message = MIMEText("This is a test e-mail message.")
        message['Subject'] = "Sending SMTP e-mail"
        message['From'] = self.sender_email
        message['To'] = self.receiver_email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
                smtpObj.starttls()
                smtpObj.login(self.sender_email, self.password)
                smtpObj.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print("Successfully sent email")
        except Exception as e:
            print("Error: unable to send email")
            print(f"Reason: {e}")

# Usage
if __name__ == "__main__":
    sender = EmailSender(
        sender_email="your_email@gmail.com",           # Replace with your Gmail address
        password="your_app_password",                  # Use an App Password, NOT your actual password
        receiver_email="recipient@gmail.com"
    )
    sender.send_email()
