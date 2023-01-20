import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.headerregistry import Address



server = smtplib.SMTP(host = 'mail.arcom.com.br', port = 587)
server.ehlo()
server.starttls()
message = 'Olá, mundo!'
email_msg = MIMEMultipart()
email_msg['From'] = "analistas@arcom.com.br"
email_msg['Subject'] = 'Assunto da mensagem'
email_msg.attach(MIMEText(message, 'plain'))
server.sendmail(email_msg['From'], ['pedro.teles@arcom.com.br', 'joao.claro@arcom.com.br'], email_msg.as_string())
server.quit()