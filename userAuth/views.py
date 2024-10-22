from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
#For sending feedback messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email):
            messages.error(request, "Account exist!")
            return render(request, 'auth/register.html')

        user = User(
            username = username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
      
        user.set_password(password)

        user.save()

        return redirect('signin')


    return render(request, 'auth/register.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Find the user by email
            user = User.objects.get(email=email)

            # Check if the provided password matches the hashed password
            if user.check_password(password):
                login(request, user)  # Log the user in

                # Store user ID and email in session
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email

                return redirect('dashboard')  # Redirect to dashboard
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials')

    return render(request, 'auth/login.html')


