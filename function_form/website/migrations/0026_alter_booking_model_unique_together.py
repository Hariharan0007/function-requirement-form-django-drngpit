# Generated by Django 4.1.3 on 2023-02-17 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_function_model_func_students_external_class_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking_model',
            unique_together=set(),
        ),
    ]
