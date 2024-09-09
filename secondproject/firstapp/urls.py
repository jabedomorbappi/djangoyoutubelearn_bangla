

from django.urls import path
from .views import firstApp,data,success_view

urlpatterns = [
   
    path('', firstApp,name="firstapp"),
    path('data/', data,name="data_form"),
    path('success/',success_view,name='success')
]
