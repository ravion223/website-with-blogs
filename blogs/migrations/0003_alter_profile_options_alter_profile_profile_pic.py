# Generated by Django 5.0.3 on 2024-03-17 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['date_of_creation'], 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank='True', default='C:\\Users\\Пользователь\\Documents\\Actual_Python\\DJANGO_PET_PROJ\\website-with-blogs\\static\\img\\default-profile-pic.jpg', null=True, upload_to='profile/'),
        ),
    ]