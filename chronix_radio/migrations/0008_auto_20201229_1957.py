# Generated by Django 3.1.4 on 2020-12-29 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chronix_radio', '0007_auto_20201229_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronixAggressionTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ChronixGritTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ChronixMetalTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ChronixRadioTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('album_name', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('favourite', models.BooleanField(default=False)),
                ('counter', models.IntegerField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='chronixgrit',
            name='track',
        ),
        migrations.RemoveField(
            model_name='chronixmetal',
            name='track',
        ),
        migrations.RemoveField(
            model_name='chronixradio',
            name='track',
        ),
        migrations.DeleteModel(
            name='ChronixAggression',
        ),
        migrations.DeleteModel(
            name='ChronixGrit',
        ),
        migrations.DeleteModel(
            name='ChronixMetal',
        ),
        migrations.DeleteModel(
            name='ChronixRadio',
        ),
        migrations.DeleteModel(
            name='Tracks',
        ),
        migrations.AddField(
            model_name='chronixradiotrack',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chronix_radio.track'),
        ),
        migrations.AddField(
            model_name='chronixmetaltrack',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chronix_radio.track'),
        ),
        migrations.AddField(
            model_name='chronixgrittrack',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chronix_radio.track'),
        ),
        migrations.AddField(
            model_name='chronixaggressiontrack',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chronix_radio.track'),
        ),
    ]