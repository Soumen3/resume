from django.shortcuts import render

# Create your views here.
def services(request):
    cntxt={
        'activeServices':'active',
    }
    return render(request, 'serv/services.html', context=cntxt)