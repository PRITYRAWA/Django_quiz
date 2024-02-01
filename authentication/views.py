from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            login_url = reverse('user_login')
            return redirect(login_url)
    else:
        form = RegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz_page')
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})
