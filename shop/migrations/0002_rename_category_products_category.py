# Generated by Django 4.2.7 on 2024-01-02 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products", old_name="Category", new_name="category",
        ),
    ]
