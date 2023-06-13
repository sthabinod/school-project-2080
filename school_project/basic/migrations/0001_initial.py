# Generated by Django 4.1.9 on 2023-06-12 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
                ("comments", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Events",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("venue", models.CharField(max_length=100)),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Events",
                "verbose_name_plural": "Events",
            },
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("feedback", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="GalleryCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MoreAbout",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("paragraph", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("created_date", models.DateField()),
            ],
            options={
                "verbose_name": "News",
                "verbose_name_plural": "News",
            },
        ),
        migrations.CreateModel(
            name="PhoneNumber",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("phone_number", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("image", models.ImageField(blank=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Information",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("school_name", models.CharField(max_length=100)),
                ("sayings", models.CharField(max_length=100)),
                ("sayings_description", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("about_school", models.CharField(max_length=200)),
                ("more_about", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="basic.moreabout")),
                (
                    "phone_number",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="basic.phonenumber"),
                ),
            ],
            options={
                "verbose_name": "School Info",
                "verbose_name_plural": "School Info",
            },
        ),
    ]
