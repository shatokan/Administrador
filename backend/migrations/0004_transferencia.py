# Generated by Django 2.1.1 on 2018-10-01 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_bicicleta_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, choices=[('aceptado', 'Aceptado'), ('rechazado', 'Rechazado')], max_length=10)),
                ('mensaje', models.TextField()),
                ('bicicleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Bicicleta')),
                ('usuario_desde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_transferencias', to=settings.AUTH_USER_MODEL)),
                ('usuario_hacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfernecias_para_mi', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]