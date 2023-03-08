from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import locale #to translate month name to Portuguese
from datetime import datetime
from .models import Aniversariante
from datetime import date

# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'core/home.html', context )
    else:
        return render(request,'accounts/' )

@login_required
def lista_aniversariantes(request):
    mes_atual = date.today.month
    aniversariantes = Aniversariante.objects.filter(data_nascimento__month=mes_atual)
    context = {'aniversariantes': aniversariantes}
    
    return render(request, 'template.html', context)
