from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Company(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    esg_report = models.URLField(blank=True)

    def __str__(self):
        return self.symbol