# Generated by Django 4.1.4 on 2022-12-22 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.ImageField(default=1, upload_to='actors/'),
            preserve_default=False,
        ),
    ]
