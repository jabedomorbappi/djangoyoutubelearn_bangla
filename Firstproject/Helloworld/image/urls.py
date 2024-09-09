from django.urls import path
from .views import create_image_description, success_page

urlpatterns = [
    path('upload/', create_image_description, name='upload_image'),
    path('success/', success_page, name='success_page'),
]
