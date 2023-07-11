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
        #remove password
        user.set_unusable_password()
        # save user to thedb
        user.save(using=self._db)
        return user
    def create_superuser(self, email, first_name, last_name, gender,phone_number):
        pass

class User(AbstractBaseUser):

    """ custome user model"""
    email=models.EmailField(verbose_name='email address', max_length=255, unique=True, primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    phone_number=models.CharField(max_length=15)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=["first_name","last_name","gender","phone_number"]

    def __str__(self):
        return self.email
    

# panorbit-task-final-main/apps/search/models.py

from django.db import models

class Country(models.Model):
    CONTINENTS = [
        ('Asia', 'Asia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('Africa', 'Africa'),
        ('Oceania', 'Oceania'),
        ('Antarctica', 'Antarctica'),
        ('South America', 'South America'),
    ]
    
    Code = models.CharField(max_length=3, primary_key=True)
    Name = models.CharField(max_length=52)
    Continent = models.CharField(max_length=13, choices=CONTINENTS, default='Asia')
    Region = models.CharField(max_length=26)
    SurfaceArea = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    IndepYear = models.SmallIntegerField(null=True, blank=True)
    Population = models.IntegerField(default=0)
    LifeExpectancy = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    GNP = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    GNPOld = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    LocalName = models.CharField(max_length=45)
    GovernmentForm = models.CharField(max_length=45)
    HeadOfState = models.CharField(max_length=60, null=True, blank=True)
    Capital = models.IntegerField(null=True, blank=True)
    Code2 = models.CharField(max_length=2)


class City(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=35)
    CountryCode = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='CountryCode')
    District = models.CharField(max_length=20)
    Population = models.IntegerField(default=0)


class CountryLanguage(models.Model):
    OFFICIAL_STATUS = [
        ('T', 'True'),
        ('F', 'False'),
    ]

    CountryCode = models.ForeignKey(Country, on_delete=models.CASCADE, db_column='CountryCode')
    Language = models.CharField(max_length=30)
    IsOfficial = models.CharField(max_length=1, choices=OFFICIAL_STATUS, default='F')
    Percentage = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)

    class Meta:
        unique_together = (('CountryCode', 'Language'),)

