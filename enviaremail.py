#Enviar email con Python
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart

# CONFIGURACIÓN DEL SERVIDOR SMTP
smtp_server = "mail.devwapps.com" #O tu servidor smtp de Gmail
smtp_port = 587 # Puerto para TLS
smtp_user = "info@devwapps.com" #O tu dirección de Gmail
smtp_password = "Ag98b3nz0" # Tu clave de correo electrónico

# Crear el mensaje y el receptor
subject = "Hola, te escribo desde mi programa de Python"
body = "ESpero que encuentres este curso interesante"
sender_email = "info@devwapps.com"
receiver_email = "emoralest@gmail.com" #La persona que recibe el correo

# CREAR EL OBJETO MULTIPART 
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
#Hack , sin la fecha el scritp lanza error
message['Date'] = formatdate(localtime = True)

# Adjuntar el mensaje
message.attach(MIMEText(body, 'plain')) #O HTML según sea el caso

# Iniciar la conexión al servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() #Iniciar el modo seguro TLS
    server.login(smtp_user, smtp_password) #Inciar sesión en el servidor smtp
    text = message.as_string() #Convertir el mensaje a texto
    server.sendmail(sender_email, receiver_email, text) #Enviar  el correo
    print("Correo enviado con éxito")
except Exception as e:
    print(f'Error al enviar el correo. Causa: {e}')
finally:
    server.quit() #Cerrar la conexión al servidor SMTP
