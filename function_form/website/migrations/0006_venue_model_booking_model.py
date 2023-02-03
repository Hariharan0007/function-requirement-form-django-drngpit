# Generated by Django 4.1.3 on 2022-11-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_function_model_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='venue_model',
            fields=[
                ('venue', models.CharField(max_length=60, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='booking_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=60)),
                ('booking_date', models.DateField()),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
            ],
            options={
                'unique_together': {('venue', 'booking_date', 'starting_time')},
            },
        ),
    ]
