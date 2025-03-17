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
    # this permission method is used to check if the user has app level permissions
    # since it it true the user has all permissions
    def has_module_perms(self,app_label):
        return True
    

class AppplicantProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    bio = RichTextField(null = True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    Phone = models.CharField(max_length=14, null=True, blank=True)
    gender = models.CharField(max_length=255,choices=GENDER_CHOICES, null=True, blank=True)
    website = models.CharField(max_length=255, null=True,blank=True)
    resume = models.FileField(null=True, blank=True)
    totalViewCount = models.IntegerField(default=0, null=True, blank=True)

class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    about = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    totalViewCount = models.IntegerField(null=True, blank=True) 


    





    

