from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    #Стандартные поля (username, email, password, first_name, last_name)
    middle_name = models.CharField(max_length=100, blank=True, default='', verbose_name='Отчество')
