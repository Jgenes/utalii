from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AccountVerification, UploadedFile



# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    # Access session data
    user_id = request.session.get('user_id')  # Get user ID from session
    username = request.session.get('user_email')  # Get user email from session
    name = request.session.get('user_name')  # Get user email from session

    if user_id is None or username is None:
        # This should not happen if the user is logged in properly
        messages.error(request, 'User data not found in session.')
        #return redirect('')  # Redirect to login if session data is missing

    return render(request, 'dashboard/index.html', {'user_id': user_id, 'username': username, 'name': name})

@login_required
def verify_account(request):
    if request.method == 'POST':
        operator_name = request.POST.get('operator_name')
        url = request.POST.get('url')
        address = request.POST.get('address')

        # Create the AccountVerification instance
        account = AccountVerification(
            operator_name=operator_name,
            url=url,
            address=address,
            user=request.user  # Associate with the logged-in user
        )
        account.save()  # Save to the database

        # Handle multiple file uploads
        for uploaded_file in request.FILES.getlist('files'):
            UploadedFile.objects.create(verification_account=account, file=uploaded_file)

        messages.success(request, 'Your account verification request has been submitted.')
        return redirect('dashboard')  # Redirect to a desired view

    return render(request, 'verify_account.html')
