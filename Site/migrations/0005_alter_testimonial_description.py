# Generated by Django 4.0.5 on 2022-06-09 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0004_testtitle_remove_testimonial_section_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='description',
            field=models.TextField(),
        ),
    ]