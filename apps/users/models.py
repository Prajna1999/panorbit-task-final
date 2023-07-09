from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):

    #create a generic user
    def create_user(self, email, first_name, last_name, gender,phone_number):
        # error handling
        if not email:
            raise ValueError('Users must have an email address')
        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            phone_number=phone_number,

        )
        # save user to thedb
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address', max_length=255, unique=True, primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'gender', 'phone_number']

    def __str__(self):
        return self.email
