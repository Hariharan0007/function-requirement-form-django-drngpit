# Generated by Django 4.1.3 on 2022-12-04 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_function_model_organizer_mail_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='function_model',
            name='document_pdf',
            field=models.FileField(default=django.utils.timezone.now, upload_to='function_form/booking_doc'),
            preserve_default=False,
        ),
    ]