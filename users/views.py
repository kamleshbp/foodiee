from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Welcome {username}, your account is created successfully.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {
        'form': form
    })
