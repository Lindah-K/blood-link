# Generated by Django 5.0.4 on 2024-05-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_remove_contactus_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='display_contact_info',
            field=models.TextField(default=''),
        ),
    ]