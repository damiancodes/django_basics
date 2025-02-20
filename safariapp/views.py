from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "aboutus.html")

def service(request):
    return render(request, 'services.html')
