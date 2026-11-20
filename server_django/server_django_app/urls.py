from django.urls import path
from .views import index, register_step1, register_step2


urlpatterns = [
    path('index/', index, name='index'),
    path('register', register_step1, name='register_step1'),
    path('register/credentials/', register_step2, name='register_step2'),
]
