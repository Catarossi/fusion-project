from django import forms
from django.core.mail.message import EmailMessage

class FormContato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100,)
    email = forms.EmailField(label='E-mail',)
    assunto = forms.CharField(label='Assunto', max_length=100,)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Mensagem: {nome}\nEmail:{email}\nAssunto:{assunto}\nMensagem:{mensagem}'

        mail = EmailMessage(
            subject = assunto,
            body = conteudo ,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],
        headers= {'reply_to' : email}
        )

        mail.send()