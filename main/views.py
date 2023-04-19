from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Validate form data
        if not username or not password or not email:
            messages.error(request, 'All fields are required.')
            return redirect('signup')
        
        # Create new user account
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')
    
    return render(request, 'signup.html')


from django.shortcuts import render, redirect
from .models import User

def login(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        try:
            user = User.objects.get(username=username, password=password)
            # Redirect to home page
            return redirect('home')
        except User.DoesNotExist:
            # Display error message
            error = "Invalid username or password"
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')
