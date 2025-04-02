from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField

# User Type Choices
USER_TYPES = [
    ('applicant', 'Applicant'),
    ('company', 'Company'),
]

# Creating custom user manager
class CustomManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a name")
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, name, email, password):
        user = self.create_user(
            name = name,
            email = self.normalize_email(email),
            password = password,
            )
        
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Creating custom user model
class CustomUserModel(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True) 
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, blank=True, null=True)  
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin  # Only allow admin users full permissions
    
    def has_module_perms(self, app_label):
        return self.is_admin

# Applicant Profile
class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='applicant_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = RichTextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

# Company Profile
class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='company_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = RichTextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

# Job Model
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='jobs')
    location = models.CharField(max_length=255, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
