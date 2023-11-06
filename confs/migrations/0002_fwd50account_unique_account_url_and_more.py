# Generated by Django 4.2.7 on 2023-11-06 14:46

from django.db import migrations, models


def clear_tables(_, __):
    ...


def run_stattag(*_, **__):
    ...


class Migration(migrations.Migration):
    dependencies = [
        ("confs", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(clear_tables),
        migrations.AddConstraint(
            model_name="fwd50account",
            constraint=models.UniqueConstraint(fields=("url",), name="unique_account_url"),
        ),
        migrations.AddConstraint(
            model_name="fwd50post",
            constraint=models.UniqueConstraint(fields=("url",), name="unique_post_url"),
        ),
        migrations.RunPython(run_stattag),
    ]
