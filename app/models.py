from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    cpf_usuario = models.CharField(max_length=14, blank=True, null=True, default=None, unique=True)

class Servicos(models.Model):
    servico = models.CharField(max_length=120, blank=True, null=True, default=None)

class GerarPedido(models.Model):
    nome_usuario = models.CharField(max_length=120, blank=True, null=True, default=None)
    servico_pedido = models.CharField(max_length=120, blank=True, null=True, default=None)
    telefone = models.CharField(max_length=15, blank=True, null=True, default=None)
    observacoes = models.CharField(max_length=200, blank=True, null=True, default=None)