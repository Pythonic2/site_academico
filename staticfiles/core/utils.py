from mysite import settings
from email.message import EmailMessage
import smtplib

class EnviarEmail():

    @classmethod
    def enviar_email(cls,nome,email,phone,menssagem):
        msg = EmailMessage()
        msg['subject'] = f'{nome}'
        msg['From'] = settings.EMAIL_ADDRESS
        msg['To'] = 'igormarinhosilva@gmail.com'
        
        msg.set_content(f'Novo Contato: {nome}.\nEmail: {email}.\nPhone: {phone}.\nMenssagem: {menssagem}.')

        with smtplib.SMTP_SSL('mail.cosmicviewpoint.com',465) as smtp:
            smtp.login(settings.EMAIL_ADDRESS,settings.EMAIL_PASSWORD)
            smtp.send_message(msg)