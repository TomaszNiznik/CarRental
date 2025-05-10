# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Widok rejestracji
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cars:index')  # Przekierowanie na stronę główną
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Widok logowania
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cars:index')  # Przekierowanie na stronę główną
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Widok wylogowywania
def logout_view(request):
    logout(request)
    return redirect('cars:index')  # Przekierowanie na stronę główną
