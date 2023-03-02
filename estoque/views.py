from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import locale #to translate month name to Portuguese
from datetime import datetime

#Create your views here.
@login_required
def estoque(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/home.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def cadastro(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/cadastro.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def ferramentaria(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/ferramentaria.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def segregados(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/segregados.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def inventario(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/inventario.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def movestoque(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/movestoque.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def precos(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/precos.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def relatorios(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/relatorios.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def leitesteira(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/leitesteira.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def leitdocasaida(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/leitdocasaida.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def aplyromaneioid(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/aplyromaneioid.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def geraprodleitor(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/geraprodleitor.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def verifnotas(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/verifnotas.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def tesembalprod(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'estoque/tesembalprod.html', context )
    else:
        return render(request,'accounts/' )

 




