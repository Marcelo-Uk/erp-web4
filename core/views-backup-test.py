from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated and request.user.groups.filter(name=['Comercial', 'Estoque']).exists() and request.user.groups.filter(name=['Mulher','Homem']):
        return render(request,'core/home.html')
    
    else:
        return render(request,'accounts/')

# def comercial(request):
#     if request.user.is_authenticated and 
#          return render(request,'core/comercial.html')

# def estoque(request):
#     if request.user.is_authenticated and request.user.groups.filter(name='Estoque').exists() and request.user.groups.filter(name='Mulher').exists() and request.user.groups.filter(name='Homem'):
#          return render(request,'core/estoque.html')   



# Estou testando direcionamento com de acordo com departamento e sexo
# Preciso testar se isso acontecerá na home, ou direto depois do login

# Estou seguindo resposta do Chat GPT
