from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichtextField

# for managing authentication of users and superusers
class MyCustomUserManager(BaseUserManager):
    # defines the required fields for creating a user
    # self refers to an instance of the class
    def create_user(self,email,name,password=None):
        # email and name validation checks
        if not email:
            raise ValueError('Must have an email address')
        if not name:
            raise ValueError('Must Have a name')
        # this creates a user instance using the model using email and name
        user = self.model(
            # converting the email to lowercase for consistency
            email=self.normalize_email(email),
            # setitng the name attribute directly to the name parameter
            name=name,
        )
        # setting the password for the user, also hashing the password
        user.set_password(password)
        user.save(using=self._db)
        
