from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'users/index.html')

def informacoes(request):
    return render(request, 'users/infos.html')

def historico(request):
    return render(request, 'users/historico.html')