import smtplib

from email.mime.text import MIMEText
msg=MIMEText("quinto correo enviado desde una aplicación python\n ésta es una prueba real de envio de correos desde una app en python, no devolver por favor")

msg['subject']="Prueba 5"
msg['From']="madialeja06@gmail.com"
msg['To']="michaelmaicol9999@hotmail.com"

mailserver=smtplib.SMTP('smtp.gmail.com',587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('madialeja06@gmail.com','s0y100y0m4d1')#debo probar ésto
mailserver.sendmail('michaelmaicol9999@hotmail.com','st.cardenas@udla.edu.co',msg.as_string())

mailserver.close()
