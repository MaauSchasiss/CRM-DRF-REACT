from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    ci = models.CharField(max_length=7)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=150)
    company = models.CharField(max_length=100,default='Desconocido')
    
    # Campos de seguimiento
    source = models.CharField(max_length=100,default='Desconocido')
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    
    # Campos de estado y prioridad
    priority = models.CharField(max_length=20, choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja')
    category = models.CharField(max_length=100, choices=[
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('VIP', 'VIP')
    ], default='Activo')
    
    # Campos temporales
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_purchase = models.DateTimeField(null=True, blank=True)
    
    # Relaciones y métricas
    total_purchases = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    products = models.ManyToManyField('product.Product', blank=True, related_name='clients')
    assigned_to = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_clients')
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_clients')

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.name} - {self.email}"

    def get_full_address(self):
        return self.address 

