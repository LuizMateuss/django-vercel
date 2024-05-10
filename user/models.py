from django.db import models
from django.contrib.auth.models import AbstractUser
from setup.settings import AUTH_USER_MODEL
from estate.models import Estate
class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
        
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class Administrator(models.Model):
    administrator = models.OneToOneField(AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)

class Employee(models.Model):
    employee = models.OneToOneField(AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
    realtor = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='realtor_set')
    estate = models.ForeignKey(Estate, on_delete=models.DO_NOTHING)
    is_Manager = models.BooleanField(default=False)