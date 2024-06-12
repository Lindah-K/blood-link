from django.shortcuts import render
from .models import HomePageSlider, HomePageBody



def homedisplay(request):
    home_slider = HomePageSlider.objects.get(id_number=1)

    context = {
        'home_slider' : home_slider,
     
    }

    return render(request, 'home_base.html', context)


