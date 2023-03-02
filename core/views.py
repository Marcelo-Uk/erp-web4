from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import locale #to translate month name to Portuguese
from datetime import datetime

# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated:
        
        locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')
        data_hoje = datetime.now()
        data = data_hoje.strftime('%d de %B de %Y ').capitalize()
        context={'data': data}
        return render(request,'core/home.html', context )
    else:
        return render(request,'accounts/' )