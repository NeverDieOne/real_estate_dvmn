# Generated by Django 2.2.4 on 2019-11-14 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='text',
            field=models.TextField(verbose_name='Текст жалобы'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
