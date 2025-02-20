from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('seller', 'Vendedor'),
        ('support', 'Soporte'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='seller')
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='supervised_users')

    # Añade related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']

    def get_assigned_leads_count(self):
        return self.assigned_leads.count()

    def get_active_clients_count(self):
        return self.assigned_clients.filter(is_active=True).count()



