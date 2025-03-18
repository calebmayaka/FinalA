from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class CustomUserMnaager(BaseUserManager):
    def create_user(self,name, email, password=None)
        if not email:
            raise ValueError('Email is required')
        if not name:
            raise ValueError('Name ')
        
        user = user.model(
            email = self.normalize_email(email),
            name = name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_super_user(self,name,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            name = name
        )

        user.is_admin = True