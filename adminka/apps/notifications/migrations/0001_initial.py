# Generated by Django 4.2.2 on 2023-07-20 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=155)),
                ('allow_dates', models.BooleanField(blank=True, default=True, null=True)),
                ('type', models.CharField(choices=[('success', 'Positive'), ('warning', 'Warning'), ('danger', 'Error'), ('info', 'Info')], max_length=15)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
        ),
    ]
