# Generated by Django 4.0.5 on 2022-06-21 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0013_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='comments',
            new_name='comment',
        ),
    ]