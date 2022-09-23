# Generated by Django 4.1 on 2022-09-23 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('referals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='recommended_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommended', to=settings.AUTH_USER_MODEL),
        ),
    ]