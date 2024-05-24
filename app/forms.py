from django import forms
from app.models import GerarPedido

class PedidoForms(forms.ModelForm):
    class Meta:
        model = GerarPedido
        exclude = ()