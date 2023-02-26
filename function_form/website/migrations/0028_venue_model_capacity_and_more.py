# Generated by Django 4.1.3 on 2023-02-20 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_alter_booking_model_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue_model',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='venue_model',
            unique_together={('venue', 'capacity')},
        ),
    ]
