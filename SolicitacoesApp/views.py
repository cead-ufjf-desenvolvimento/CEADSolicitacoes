from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy
from django import forms

# Importe a função message_producao do arquivo utils.py
from SolicitacoesApp.utils import message_producao

# Importe os módulos necessários do Django
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def Index(request):

    return render(request, 'SolicitacoesApp/index.html')


class ProducaoDeMaterialCreateView(CreateView) :
    model = ProducaoDeMaterial
    fields = '__all__'
    template_name = 'SolicitacoesApp/producao/create.html'
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['data_agendamento'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['horario_agendamento'].widget = forms.TimeInput(attrs={'type': 'time'})
        form.fields['data_entrega_material'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        """
        Caso o formulário seja válido, envie um e-mail com os dados do formulário para o responsável
        """
        send_mail(
            subject=f"Solicitação - {form.cleaned_data['professor_responsavel']}",  # Define o assunto do e-mail
            message=message_producao(form.cleaned_data),  # Define o corpo do e-mail usando a função message_producao
            from_email=settings.EMAIL_HOST_USER,  # Define o remetente do e-mail 
            recipient_list=['seu@email.com']  # Define os destinatários do e-mail
        )
        
        # Reseta o comportamento da classe
        return super().form_valid(form)
