from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.

class User (AbstractUser):
    #category = models.ForeignKey(Category, on_delete=models.CASCADE ,blank=False, null=False,related_name='category')
    '''
    username
    first_name
    last_name
    email
    password
    groups
    user_permissions
    is_staff
    is_active
    is_superuser
    last_login
    date_joined
    '''