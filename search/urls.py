from django.urls import path
from .views import searchdisplay, donorlistdetail

urlpatterns = [
    path('', searchdisplay, name='searchsite'),
    path('donorlist/', searchdisplay, name='donorlistsite'),
    path('donorlist/donorlistdetail/<email>/', donorlistdetail, name='donorlistdetailsite'),
]