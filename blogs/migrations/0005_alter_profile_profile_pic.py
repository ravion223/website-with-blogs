# Generated by Django 5.0.3 on 2024-03-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='/static/img/default-profile-pic.jpg', upload_to='profile/'),
        ),
    ]
