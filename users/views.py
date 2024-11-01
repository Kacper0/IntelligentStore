from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if UserProfile.object.filter(email=email).exists():
                form.add_error('email', 'Ten adres e-mail jest już zajęty.')
            else:
                user = form.save()
                UserProfile.objects.create(user=user, email=form.cleaned_data.get('email'))
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Sprawdzanie profilu użytkownika
            try:
                user_profile = user.userprofile  # Może rzucić wyjątek
                # Logika po pomyślnym logowaniu
                return redirect('home')
            except UserProfile.DoesNotExist:
                # Obsługuje brak profilu
                return render(request, 'users/login.html', {'error': 'Profil użytkownika nie istnieje'})
        else:
            return render(request, 'users/login.html', {'error': 'Błędne dane logowania'})
    return render(request, 'users/login.html')

def user_list_view(request):
    users = User.objects.all()
    print(users)
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def home_view(request):
    return render(request, 'home.html')