# Generated by Django 4.2.1 on 2023-06-18 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('cpid', models.IntegerField()),
                ('cpname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]