import smtplib

from email.mime.text import MIMEText
msg=MIMEText("mensaje del correo")

msg['subject']="asunto"
msg['From']="correo de quien envia"
msg['To']="correo de quien recive"

mailserver=smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('correo de quien envia','xxxxxxxxxx contraseña de ese correo')#debo probar ésto
mailserver.sendmail('otros destinatarios','otros destinatarios',msg.as_string())

mailserver.close()

#MITCH CODE
