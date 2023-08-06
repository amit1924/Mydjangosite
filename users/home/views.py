from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    if not request.user.is_authenticated:
        # User is anonymous
        # Perform actions for anonymous users
        return render(request, 'anonymous.html')
    else:
        # User is authenticated
        # Perform actions for authenticated users
        return render(request, 'index.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Replace 'home' with the name of your home page URL pattern
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')  # Replace 'index' with the name of your index page URL pattern
