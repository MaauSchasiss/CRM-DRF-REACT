# Generated by Django 5.1.6 on 2025-02-20 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_options_client_assigned_to_and_more'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-create_at'], 'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='adrees',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='is_active',
        ),
        migrations.AddField(
            model_name='client',
            name='category',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('VIP', 'VIP')], default='Activo', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='priority',
            field=models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta')], default='Baja', max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='clients', to='product.product'),
        ),
        migrations.AddField(
            model_name='client',
            name='source',
            field=models.CharField(default='Desconocido', max_length=100),
        ),
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
