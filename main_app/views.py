from django.shortcuts import render
from .models import Detail

# Create your views here.
def dashboard(request):
    data = Detail.objects.all()
    return render(request, 'index.html', {'data': data})