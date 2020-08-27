import smtplib, ssl
import image
import config
from email.message import EmailMessage

image.prepare_image()
port = 465  
msg= EmailMessage()
msg['From'] = config.sender
msg['To'] = config.recipients
msg['Subject'] = "Facts on Chuck Norris"

with open('image.png',"rb") as fp:
    img=fp.read()
msg.add_attachment(img, maintype="image", subtype="png")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login(config.sender,config.password)
    server.send_message(msg)

