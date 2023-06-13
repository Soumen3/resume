from django.shortcuts import render


# Create your views here.
def skill(request):
    cntxt={
        'activeSkill':'active',
    }
    return render(request, 'edu/skill.html', context=cntxt)