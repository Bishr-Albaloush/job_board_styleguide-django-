# Generated by Django 5.0.3 on 2024-03-20 23:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(default=1, upload_to="profile/"),
            preserve_default=False,
        ),
    ]
