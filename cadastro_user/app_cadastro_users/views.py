from django.shortcuts import render
from .models import Usuario # importanto a classe models Usuario
# Create your views here.
def home (request):
    return render(request,'usuarios/home.html')

def usuarios(request): # função vai pegar os dados que vem da tela
    novo_usuario = Usuario() 
    novo_usuario.nome = request.POST.get('nome') # recebendo os dados  
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save() #salvando

#Exibir todos usuarios ja cadastrados em uma nova page:

    usuarios = {
        'usuarios': Usuario.objects.all() #retornando todos os usuarios do banco de dados
    }

#retornar os dados para a pagina de listagem de ususarios:
    return render(request,'usuarios/usuarios.html', usuarios)  
