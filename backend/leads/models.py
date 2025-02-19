from django.db import models

# Create your models here.
class leads(models.Model):
    name = models.CharField(max_length=100)
    ci = models.CharField(max_length=7)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15 , blank=True , null=True)
    adrees = models.CharField(max_length=150)

    source = models.CharField(max_length=100)  # Como página web, redes sociales, etc.
    product_interest = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    status = models.CharField(max_length=50, choices=[('Nuevo', 'Nuevo'), ('Calificado', 'Calificado'), ('Convertido', 'Convertido')], default='Nuevo')
    priority = models.CharField(max_length=20, choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    last_contact = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"
