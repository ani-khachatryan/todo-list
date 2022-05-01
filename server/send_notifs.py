from database.py import RequestHandler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SendNotifications():
    email_sender_account = "todomipt@gmail.com"
    email_sender_username = "todomipt@gmail.com"
    email_sender_password = "abobaboba"
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587

    email_recepients #OP_GETUSERS user_id, email
    email_subject = "Tasks for today"


    server = smtplib.SMTP(email_smtp_server, email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)

    server = smtplib.SMTP(email_smtp_server,email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)

    for recipient in email_recepients:
        #print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative')
        message['From'] = email_sender_account
        message['To'] = recipient
        message['Subject'] = email_subject

        email_body #= "\n".merge rows of list OP_GETTASKS(user_id)
        message.attach(MIMEText(email_body, 'plain'))
        text = message.as_string()
        server.sendmail(email_sender_account,recipient,text)

    server.quit()
