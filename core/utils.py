from mysite import settings
from email.message import EmailMessage
from core.models import ContatoCliente
import smtplib, ssl

class EnviarEmail():

    @classmethod
    def enviar_email(cls, contato: ContatoCliente):
        msg = EmailMessage()
        msg['subject'] = contato.name
        msg['From'] = settings.EMAIL_ADDRESS
        msg['To'] = 'orcamentos@ciaseniorcuidar.com.br'
        
        msg.set_content(f'Novo Contato: {contato.name}.\nEmail: {contato.email}.\nPhone: {contato.phone}.\nTipo: {contato.tipo}.\nCidade: {contato.cidade}.\nMensagem: {contato.message}.')

        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT@SECLEVEL=1')  # Define o nível de segurança para evitar problemas com versões mais antigas do OpenSSL

        try:
            with smtplib.SMTP('mail.ciaseniorcuidar.com.br', 587) as smtp:
                smtp.ehlo()
                smtp.starttls(context=context)
                smtp.ehlo()
                smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
                smtp.send_message(msg)
        except Exception as e:
            # Lidar com o erro, se ocorrer
            print(f"Erro ao enviar o email: {e}")
    
        
        if contato.tipo == 'Preciso de um Cuidador':
            msg1 = EmailMessage()
            msg1['subject'] = f'Re: {contato.tipo}'
            msg1['From'] = f'Cia Sênior Cuidar <{settings.EMAIL_ADDRESS}>'
            msg1['To'] = contato.email
            msg1.set_content(f'Olá, {contato.name}. Seja bem vindo (a) a cultura Cia Sênior Cuidar, preparamos com muito carinho e dedicação cada serviço para proporcionar uma melhor atenção a você e ou seu familiar. No Prazo de até 12 horas entraremos em contato com seu Orçamento.')
    
            context1 = ssl.create_default_context()
            context1.set_ciphers('DEFAULT@SECLEVEL=1')  # Define o nível de segurança para evitar problemas com versões mais antigas do OpenSSL
    
            try:
                with smtplib.SMTP('mail.ciaseniorcuidar.com.br', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls(context=context1)
                    smtp.ehlo()
                    smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
                    smtp.send_message(msg1)
            except Exception as e:
                # Lidar com o erro, se ocorrer
                print(f"Erro ao enviar o email: {e}")
        else:
            msg1 = EmailMessage()
            msg1['subject'] = f'Re: {contato.tipo}'
            msg1['From'] = f'Cia Sênior Cuidar <{settings.EMAIL_ADDRESS}>'
            msg1['To'] = contato.email
            msg1.set_content(f'Olá, {contato.name}. Seja bem vindo (a) a cultura Cia Sênior Cuidar, em breve entraremos em contato para solicitação de currículo, mantenha-o atualizado.')
    
            context1 = ssl.create_default_context()
            context1.set_ciphers('DEFAULT@SECLEVEL=1')  # Define o nível de segurança para evitar problemas com versões mais antigas do OpenSSL
    
            try:
                with smtplib.SMTP('mail.ciaseniorcuidar.com.br', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls(context=context1)
                    smtp.ehlo()
                    smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
                    smtp.send_message(msg1)
            except Exception as e:
                # Lidar com o erro, se ocorrer
                print(f"Erro ao enviar o email: {e}")