from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class Company(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    esg_report = models.URLField(blank=True)
    yf_t_score = models.FloatField()
    yf_e_score = models.FloatField()
    yf_s_score = models.FloatField()
    yf_g_score = models.FloatField()

    def __str__(self):
        return self.symbol
    
class ETF(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    yf_t_score = models.FloatField()
    yf_e_score = models.FloatField()
    yf_s_score = models.FloatField()
    yf_g_score = models.FloatField()


    def __str__(self):
        return self.symbol