# Generated by Django 3.1.4 on 2021-01-04 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chronix_radio', '0010_auto_20201231_0427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='favourite',
        ),
        migrations.AlterField(
            model_name='track',
            name='img',
            field=models.ImageField(blank=True, upload_to='tracks/'),
        ),
    ]
