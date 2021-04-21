from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.



class CustomAccountManager(BaseUserManager):
    
    def create_user(self, email, user_name, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                _('Superuser must be staff')
            )
        if other_fields.get('is_active') is not True:
            raise ValueError(
                _('Superuser must be active')
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Superuser must be superuser')
            )
            
        return self.create_user(email, user_name, first_name, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin): #the permission mixin is necesary as we access to user permissions
    email = models.EmailField(_("Email Adress"), max_length=254, unique=True)
    user_name = models.CharField(_("Login"), max_length=50, unique=True)
    first_name = models.CharField(_("Name"), max_length=50)
    last_name = models.CharField(_("Surname"), max_length=50)
    is_staff = models.BooleanField(_("¿Staff?"), default=False)
    is_active = models.BooleanField(_("¿Active?"), default=False)
    is_superuser = models.BooleanField(_("¿Superuser?"), default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['user_name', 'first_name']
    
    objects = CustomAccountManager()
    
    def __str__(self):
        return self.email