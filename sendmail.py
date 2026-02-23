from email.message import EmailMessage
import smtplib
from os import getenv


def mailman(check_result, email_addr, hashed_pwrd):
    try:
        mmsg = EmailMessage()
        mmsg['Subject'] = 'Password checking result!'
        mmsg['From'] = 'S1L3NT1337'
        mmsg['To'] = email_addr
        mmsg.set_content(f"Result for password(sha-1): {hashed_pwrd}" +
                         '\n [ ' + check_result + ' ]')

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(getenv("SENDER_EMAIL"), getenv("EMAIL_PWRD"))
            smtp.send_message(mmsg)
    except:
        raise Exception("SMTP setup error!")
    else:
        print("SMAIL: DONE")
