from mysite import settings
from email.message import EmailMessage
from core.models import ContatoCliente
import smtplib

class EnviarEmail():

    @classmethod
    def enviar_email(cls,contato:ContatoCliente):

        msg = EmailMessage()
        msg['subject'] = contato.name
        msg['From'] = settings.EMAIL_ADDRESS
        msg['To'] = 'igormarinhosilva@gmail.com'
        
        msg.set_content(f'Novo Contato: {contato.name}.\nEmail: {contato.email}.\nPhone: {contato.phone}.\nMenssagem: {contato.message}.')

        with smtplib.SMTP_SSL('mail.cosmicviewpoint.com',465) as smtp:
            smtp.login(settings.EMAIL_ADDRESS,settings.EMAIL_PASSWORD)
            smtp.send_message(msg)