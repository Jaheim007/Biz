# Generated by Django 4.0.5 on 2022-06-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0008_delete_team_remove_started_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sevice_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img1', models.CharField(max_length=255)),
                ('img2', models.CharField(max_length=255)),
            ],
        ),
    ]
