# Generated by Django 3.1.2 on 2021-05-31 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
