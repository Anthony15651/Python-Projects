# Generated by Django 4.2.2 on 2023-06-28 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Miss', 'Miss'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], max_length=5),
        ),
    ]
