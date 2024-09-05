from django.urls import path,include
from .views import imageshow,loadimage

urlpatterns = [

    path('posts/',imageshow,name='imageshow'),
    path('load_image/',loadimage,name='load_image'),
    
]