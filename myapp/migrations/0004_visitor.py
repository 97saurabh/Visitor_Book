# Generated by Django 2.2.1 on 2019-11-25 06:14

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None)),
                ('date', models.DateField(auto_now=True)),
                ('check_in', models.TimeField(auto_now=True)),
                ('check_out', models.TimeField(blank=True, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='myapp.Host')),
            ],
        ),
    ]