import smtplib
from email.message import EmailMessage

def send_email(reciver,user_name,course_title,score,time):
    sender_email = "edusphere546@gmail.com"
    sender_password = "kikk qfxe qkoq arom"
    receiver_email = reciver

    msg = EmailMessage()
    msg["Subject"] = f"Student Performance Report – [{course_title}]"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"Hello! {user_name} \nyou had successfully completed {course_title} course \non EduSphere with {score}% \ndownload your certificate from EduSphere")

    # Connect to Gmail SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print('error to send mail:- ',e)
    

if __name__ == '__main__':
    send_email('preyanspatel84@gmail.com','preyans','python','100')