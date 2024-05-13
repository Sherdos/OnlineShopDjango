from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from user.forms import LoginForm, RegisterForm
from django.views import generic
from django.contrib.auth import login, logout
from user.models import Profie, User
# Create your views here.

class UserRegisterView(generic.CreateView):
    template_name = 'pages/login.html'  
    form_class = RegisterForm
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        
        return redirect('index')

def logout_user(request):
    logout(request)
    return redirect('index')

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'pages/login.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Войти'
        return context
    def get_success_url(self) -> str:
        return reverse_lazy('index')
    
def profile(request):
    return render(request, 'page/profile.html')

class Profile(generic.DetailView):
    template_name = 'page/profile.html'
    model = User
    context_object_name = 'user'
    
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        title = f'Профиль {context["user"].username}'
        context['profile'] = Profie.objects.get(user_id=context["user"].id)
        context['title'] = title
        return context
    
    