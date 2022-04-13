from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UserAddModel
# Create your views here.
def about(request):
    useradd = UserAddModel.objects.all()
    context = {
        'useradd':useradd
    }
    return render(request,'about.html',context)

class LoginTemplateView(TemplateView):
    template_name = 'login.html'

class RegisterTemplateView(TemplateView):
    template_name = 'register.html'