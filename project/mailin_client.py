import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_mail(sender,password,reciever,subj,body):
    msg=MIMEMultipart()
    msg['From']=sender
    msg['To']=reciever
    msg['Subject']=subj
    msg.attach(MIMEText(body,'plain'))
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.send_message(msg)
    server.quit()
    print(f"Email Sent Sucessfully to {reciever}")


     
with open ('/home/SOLO/pithon/project/pass.txt','r') as f:
    ok    = f.read().strip().replace(" ", "")
send_mail(
    sender="samiralitech.88@gmail.com",
    password=ok,
    reciever="legendexe10@gmail.com",
    subj="Testing my code",
    body="Hey this is me now writting to you!!!"
)