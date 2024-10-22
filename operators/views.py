# views.py

from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login

def create_profile(request):
    if request.method == 'POST':
        offices = request.POST.get('offices')
        size = request.POST.get('size')
        member_of = request.POST.get('member_of')
        tour_types = request.POST.get('tour_types')
        price_ranges = request.POST.get('price_ranges')
        destinations = request.POST.get('destinations')
        overview = request.POST.get('overview')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')
        website = request.POST.get('website')
        company_name = request.POST.get('company_name')  # New field
        image = request.FILES.get('image')  # Handle image upload

        profile = Profile(
            offices=offices,
            size=size,
            member_of=member_of,
            tour_types=tour_types,
            price_ranges=price_ranges,
            destinations=destinations,
            overview=overview,
            contact_email=contact_email,
            contact_phone=contact_phone,
            website=website,
            company_name=company_name,  # New field
            image=image,  # New field
            user=request.user  # Associate with the logged-in user
        )
        profile.save()
        return redirect('profile')  # Replace with your success URL
    return render(request, 'dashboard/create.html')



def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'dashboard/profile.html', {'profile': profile})
    except Profile.DoesNotExist:
         messages.info(request, 'You have not createsd a profile yet.')
         return redirect('profile')
    
    return render(request, 'dashboard/profile.html')
