import smtplib

from email.mime.text import MIMEText
msg = MIMEText("Contenido del correo")

msg['Subject'] = "Asunto del correo"
msg['From'] = "desdedonde@gmail.com"
msg['To'] = "haciadonde@gmail.com"

mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('leo.as10@gmail.com','CRISTOREYMARISTAS2003-')
mailServer.sendmail('leo.as10@gmail.com','leo.as10@gmail.com',msg_as_string())
mailServer.close()
