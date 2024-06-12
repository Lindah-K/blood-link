from django.shortcuts import render
from .models import AboutUs

def about_us(request):
    about_details = AboutUs.objects.first()  # Fetching the first AboutUs object
    return render(request, 'about_us.html', {'about_details': about_details})
