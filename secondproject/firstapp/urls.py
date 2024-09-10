

from django.urls import path
from .views import firstApp,data,success_view,postview
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
   
    path('', firstApp,name="firstapp"),
    path('data/', data,name="data_form"),
    path('success/',success_view,name='success'),
    path('datashow/',postview,name='datashow'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
