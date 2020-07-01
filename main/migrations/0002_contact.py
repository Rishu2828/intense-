# Generated by Django 3.0.6 on 2020-06-23 07:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('contact_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('message', models.TextField()),
            ],
        ),
    ]
