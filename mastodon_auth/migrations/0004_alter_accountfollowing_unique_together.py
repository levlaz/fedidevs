# Generated by Django 5.0.3 on 2024-04-03 01:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0016_alter_accountlookup_language"),
        ("mastodon_auth", "0003_accountfollowing"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="accountfollowing",
            unique_together={("account", "url")},
        ),
    ]
