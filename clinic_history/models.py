from django.db import models

# Create your models here.
class History(models.Model):
    disease = models.CharField(max_length=255)
    surgery = models.CharField(max_length=255)
    medication = models.CharField(max_length=255)