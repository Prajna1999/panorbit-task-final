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
