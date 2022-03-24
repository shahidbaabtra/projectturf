# Generated by Django 4.0 on 2022-03-23 17:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('court_name', models.CharField(max_length=30)),
                ('sports_type', models.CharField(max_length=20)),
                ('phone_no', models.CharField(max_length=15)),
                ('booking_no', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=20)),
                ('status', models.CharField(default='requested', max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to='background/')),
                ('first_image', models.ImageField(blank=True, null=True, upload_to='turf/first')),
                ('second_image', models.ImageField(blank=True, null=True, upload_to='turf/second')),
                ('third_image', models.ImageField(blank=True, null=True, upload_to='turf/third')),
            ],
            options={
                'db_table': 'owners',
            },
        ),
        migrations.CreateModel(
            name='Slote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('slote', models.TimeField()),
                ('status', models.CharField(max_length=10)),
                ('turf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.owners')),
            ],
            options={
                'db_table': 'slote',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment', models.FloatField()),
                ('status', models.CharField(max_length=10)),
                ('slote_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.slote')),
                ('turf_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.owners')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]