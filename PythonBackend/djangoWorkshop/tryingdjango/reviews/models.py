from django.db import models

# Create your models here.
class Review(models.Model):
    review_text = models.CharField(max_length=100, blank=True)
    name_text = models.CharField(max_length=100, blank=True)
    email_text = models.CharField(max_length=100, blank=True)
    number_text = models.CharField(max_length=100, blank=True)