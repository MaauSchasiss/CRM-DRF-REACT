from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    ci = models.CharField(max_length=7)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15 , blank=True , null=True)
    adrees = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name

