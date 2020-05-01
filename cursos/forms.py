from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_temmplate

class ContatoCurso(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    e_mail = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)

    def send_mail(self, curso):
        subject = '{curso} contato'.format(
            curso=curso
        )
        context = {
            'nome': self.cleaned_data['nome'],
            'e_mail': self.cleaned_data['e_mail'],
            'mensagem': self.cleaned_data['mensagem']
        }
        template_name = 'cursos/email_contato.html'
        send_mail_temmplate(subject,template_name,context, [settings.CONTACT_EMAIL])


