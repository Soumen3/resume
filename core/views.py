from django.shortcuts import render

# Create your views here.
def home(request):
    cntxt={
        'activeHome':'active',
    }
    return render(request,'core/home.html', context=cntxt)


def contact(request):
    cntxt={
        'activeContact':'active',
    }
    return render(request,'core/contact.html', context=cntxt )


