from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    
    
    # Specify unique related_name for groups
    #groups = models.ManyToManyField(
    #    'auth.Group',
    #    related_name='custom_user_groups',
    #    blank=True,
    #    verbose_name='groups',
   # )
    
    # Specify unique related_name for user_permissions
   # user_permissions = models.ManyToManyField(
    #    'auth.Permission',
    #    related_name='custom_user_permissions',
    #    blank=True,
    #    verbose_name='user permissions',
   # )
