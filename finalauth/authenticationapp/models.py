from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxvalueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        if email is None:
            raise ValueError('User Must have an email address')
        if name is None:
            raise ValueError('User Must have a name')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_super_user(self,name,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_applicant = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # calling the custom user manager
    objects = CustomUserManager()

    # str dunder method to return the email when the user object is called
    def __str__(self):
        return self.email
    
    # The has_perm method is used to check if a user has a specific permission.
    # perm if the type of permission being checked and obj is the object the permission is being checked on
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    
    





    

