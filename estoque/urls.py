from django.urls import path, include
from . import views

# Create your views here.

urlpatterns = [
    path('estoque/', views.estoque, name='estoque11'),
    path('estoque/menu25', views.cadastro, name='estoque25'),
    path('estoque/menu759', views.ferramentaria, name='estoque759'),
    path('estoque/menu695', views.segregados, name='estoque695'),
    path('estoque/menu420', views.inventario, name='estoque420'),
    path('estoque/menu462', views.movestoque, name='estoque462'),
    path('estoque/menu542', views.precos, name='estoque542'),
    path('estoque/menu508', views.relatorios, name='estoque508'),
    path('estoque/menu339', views.leitesteira, name='estoque339'),
    path('estoque/menu370', views.leitdocasaida, name='estoque370'),
    path('estoque/menu384', views.aplyromaneioid, name='estoque384'),
    path('estoque/menu474', views.geraprodleitor, name='estoque474'),
    path('estoque/menu484', views.verifnotas, name='estoque484'),
    path('estoque/menu613', views.tesembalprod, name='estoque613'),
    
    path('accounts/', include('django.contrib.auth.urls'))
]