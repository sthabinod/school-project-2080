# Generated by Django 4.1.9 on 2023-07-07 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0024_aboutschool_alter_information_about_school"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="information",
            name="about_school",
        ),
        migrations.RemoveField(
            model_name="information",
            name="director_message",
        ),
        migrations.RemoveField(
            model_name="information",
            name="principal_message",
        ),
        migrations.AddField(
            model_name="aboutschool",
            name="school",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="basic.information"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="directormessage",
            name="school",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="basic.information"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="principalmessage",
            name="school",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="basic.information"),
            preserve_default=False,
        ),
    ]
