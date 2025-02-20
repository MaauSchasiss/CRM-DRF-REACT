from django.db import models

# Create your models here.
class Leads(models.Model):
    name = models.CharField(max_length=100)
    ci = models.CharField(max_length=7)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15 , blank=True , null=True)
    adrees = models.CharField(max_length=150)
    company = models.CharField(max_length=100,default='Desconocido')

    source = models.CharField(max_length=100,default='Desconocido')  # Como página web, redes sociales, etc.
    product_interest = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    status = models.CharField(max_length=50, choices=[('Nuevo', 'Nuevo'), ('Calificado', 'Calificado'), ('Convertido', 'Convertido')], default='Nuevo')
    priority = models.CharField(max_length=20, choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    last_contact = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    assigned_to = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_leads')
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='created_leads')
    client = models.ForeignKey('client.Client', on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')
    category = models.CharField(max_length=100, choices=[
        ('Potencial', 'Potencial'),
        ('No interesado', 'No interesado'),
        ('En seguimiento', 'En seguimiento')
    ], default='Potencial')
    
    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-created_at']
