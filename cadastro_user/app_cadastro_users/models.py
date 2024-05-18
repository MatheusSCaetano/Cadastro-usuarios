from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) #será gerado sequencialmente campos numeriocos nao duplicaveis -> id_ususario recebe
    nome = models.TextField(max_length=200) #noime sera tipo tex com no maximo 200 caracteres 
    idade = models.IntegerField() #idade sera do tipo int