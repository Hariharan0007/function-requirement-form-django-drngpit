# Generated by Django 4.1.3 on 2023-02-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_function_model_func_students_external'),
    ]

    operations = [
        migrations.AddField(
            model_name='function_model',
            name='func_students_external_class',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='function_model',
            name='remarks',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
