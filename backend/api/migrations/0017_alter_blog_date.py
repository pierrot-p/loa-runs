# Generated by Django 4.1 on 2022-08-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_alter_blog_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateField(verbose_name="Date"),
        ),
    ]
