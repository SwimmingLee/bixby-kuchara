# Generated by Django 2.2.6 on 2019-10-17 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=50)),
                ('movieRating', models.CharField(max_length=20)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('genre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'movies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='NamedPointStructres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Theaters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theaterName', models.CharField(max_length=20)),
                ('regionCode', models.IntegerField()),
                ('theaterCode', models.IntegerField()),
                ('longitude', models.FloatField()),
                ('raditude', models.FloatField()),
                ('brand', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'theaters',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MovieSchedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=20)),
                ('totalSeat', models.IntegerField()),
                ('availableSeat', models.IntegerField()),
                ('movieCode', models.IntegerField()),
                ('startTime', models.CharField(max_length=10)),
                ('endTime', models.CharField(max_length=10)),
                ('subtitile', models.BooleanField()),
                ('dubbing', models.BooleanField()),
                ('digitalized', models.BooleanField()),
                ('lateNight', models.BooleanField()),
                ('morning', models.BooleanField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MovieSchedules', to='movies.Movies')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.Theaters')),
            ],
            options={
                'db_table': 'movieschedules',
                'managed': True,
            },
        ),
    ]
