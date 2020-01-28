# Generated by Django 2.2.1 on 2019-11-23 22:29

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact Phone Number', max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None),
        ),
    ]
