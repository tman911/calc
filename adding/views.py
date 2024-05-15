from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        result = int(num1) + int(num2)
        return render(request, 'result.html', {'result': result})
    else:
        return HttpResponse('Method not allowed')
