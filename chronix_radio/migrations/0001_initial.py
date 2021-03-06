# Generated by Django 3.1.4 on 2020-12-16 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('played_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
