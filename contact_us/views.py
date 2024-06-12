from django.shortcuts import render
from .models import ContactDetails

def contact_us(request):
    contact_details = ContactDetails.objects.first()  # Fetching the first ContactUs object
    return render(request, 'contact_us.html', {'contact_details': contact_details})


