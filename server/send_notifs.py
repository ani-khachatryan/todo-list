from database import RequestHandler
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SendNotifications():
    email_sender_account = "todomipt@gmail.com"
    email_sender_username = "todomipt@gmail.com"
    email_sender_password = "abobaboba"
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587

    email_recepients = RequestHandler("GET_USERS")
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
        message['To'] = recipient[1]
        message['Subject'] = email_subject
        sended_tasks = RequestHandler(f"TASK_GET {recipient[0]} {datetime.today().strftime('%Y-%m-%d')}")
        send_list = []
        numeration = 1
        for task in sended_tasks:
            send_list.append(f"{numeration}. {task[2]}")
            numeration += 1
        email_body = '\n'.join(send_list) #= "\n".merge rows of list OP_GETTASKS(user_id)
        message.attach(MIMEText(email_body, 'plain'))
        text = message.as_string()
        server.sendmail(email_sender_account,recipient[1],text)

    server.quit()
