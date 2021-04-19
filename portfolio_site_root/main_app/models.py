from django.db import models


# Create your models here.

class tickets(models.Model):
    subject = models.CharField("Subject",max_length=100)
    email = models.EmailField("Email",max_length=100)
    name = models.CharField("Name",max_length=100)
    company = models.CharField("Company",max_length=100)
    phone = models.CharField("Phone",max_length=100)
    ticket = models.TextField("Ticket",max_length=250)