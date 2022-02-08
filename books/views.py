from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'y.html')
def log(request):
    return render(request,'x.html')