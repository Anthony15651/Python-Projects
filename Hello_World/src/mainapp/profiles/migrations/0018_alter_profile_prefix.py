# Generated by Django 4.2.2 on 2023-06-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(blank=True, choices=[('Miss', 'Miss'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Mr.', 'Mr.')], max_length=5),
        ),
    ]
