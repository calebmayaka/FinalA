#  main app models
#  imports
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator

# creating a custom User Manager

class CustomManager(BaseUserManager):
    # method for normal user
    def create_user(self,name,email,password=None):
        # validation checks for only required fields
        if not email:
            raise ValueError('Email is Required')
        if not name:
            raise ValueError('name is Required')
        #creating the user, also using the two fields, email and password
        #  i have normalized the email to convert it to lowercase
        user = self.model(
            email = self.normalize_email(email),
            name = name,
        )
        # setting the password
        user.set_password(password)
        # saving the user to the database
        user.save(using=self._db)

        # returning the user
        return user
    
    # method for creating a superuser
    def create_super_user(self,name,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            name = name,
            password = password,
        )
        # setting the user as staff and admin
        user.is_staff = True
        user.is_admin = True

        # saving and returning the user
        # no need to use the set_password because the password is already set
        user.save(using=self._db)
        return user
    
# creating the custom user model

class CustomModel(AbstractBaseUser):
    # creating the fields for the custom user model
    # usinh unique = True to make sure that the email is unique, hence the primary key
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    # adding the fields for the user type   
    is_applicant = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    # adding the fields for the user permissions, cheching whether a user is active, staff or an admin
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # setting the email as the username field
    USERNAME_FIELD = 'email'
    # list if required fields
    REQUIRED_FIELDS = ['name']

    # creating the user manager
    objects = CustomManager()

    # dunder methods
    
    # return the email when an instance of the class is called 
    def __str__(self):
        return self.email

    # check whether a user has specific permissions
    # has three parameters, self, perm - type of permission, obj=None.
    def has_perm(self,perm, obj=None):
        return True
    
    # check whether users have soecific app permissions
    def has_module_perms(self,app_label):
        return True

class applicantprofile(models.Model):
    image_types = ['.jpg', '.png', '.jpeg' ,'.jiff']
    
    user = models.OneToOneField(CustomModel,null=True, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, type = image_types)
    description = models.TextField(null=True, blank=True, max_length=255)
    content = RichTextField(null=True, max_length = 255, blank=True)
    
    # social media links
    linkedin = models.TextField(max_length=255, null=True, blank=True)
    twitter  = models.TextField(max_length=255, null=True, blank=True)
    facebook =  models.TextField(max_length=255, null=True, blank=True)
    reddit = models.TextField(max_length=255, null=True, blank=True)

class companyprofile(models.Model):
    # this means that a user can only have one profile and a profile can only belong to one user
    # enforcing the one to one relationship
    user = models.OneToOneField(CustomModel, null=True, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=255)
    content = RichTextField(null=True, max_length = 255, blank=True)
    
    
