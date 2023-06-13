# Generated by Django 4.1.9 on 2023-06-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0013_contact_map"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="map",
        ),
        migrations.AddField(
            model_name="information",
            name="map",
            field=models.URLField(blank=True, null=True),
        ),
    ]