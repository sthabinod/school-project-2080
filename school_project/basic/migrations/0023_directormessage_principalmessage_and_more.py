# Generated by Django 4.1.9 on 2023-07-07 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0022_information_director_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DirectorMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("director_message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="PrincipalMessage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("principal_message", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="information",
            name="director_message",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="basic.directormessage"),
        ),
        migrations.AlterField(
            model_name="information",
            name="principal_message",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="basic.principalmessage"),
        ),
    ]
