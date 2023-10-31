import smtplib, ssl

def send_email(message):
    host = "smtp.stackmail.com"
    port = 465

    username = "reyner@reynerveliz.com"
    password = "RB1=u^`}?&_@"

    receiver = "reyner@reynerveliz.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)