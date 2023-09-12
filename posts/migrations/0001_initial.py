# Generated by Django 4.2.5 on 2023-09-12 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("posts", "0001_initial"),
        ("posts", "0002_alter_post_unique_together_alter_post_senstive"),
        ("posts", "0003_alter_post_card"),
        ("posts", "0004_alter_post_reblog"),
        ("posts", "0005_alter_post_language"),
        ("posts", "0006_alter_post_application"),
    ]

    dependencies = [
        ("accounts", "0012_alter_accountlookup_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_id", models.TextField()),
                ("instance", models.TextField()),
                ("created_at", models.DateTimeField()),
                ("in_reply_to_id", models.TextField(blank=True, null=True)),
                ("in_reply_to_account_id", models.TextField(blank=True, null=True)),
                ("senstive", models.BooleanField(blank=True, null=True)),
                ("spoiler_text", models.TextField(blank=True, null=True)),
                ("visibility", models.TextField()),
                ("language", models.TextField(blank=True, null=True)),
                ("uri", models.URLField()),
                ("url", models.URLField()),
                ("replies_count", models.IntegerField()),
                ("reblogs_count", models.IntegerField()),
                ("favourites_count", models.IntegerField()),
                ("edited_at", models.DateTimeField(blank=True, null=True)),
                ("content", models.TextField()),
                ("application", models.JSONField(blank=True, null=True)),
                ("media_attachments", models.JSONField(default=list)),
                ("mentions", models.JSONField(default=list)),
                ("tags", models.JSONField(default=list)),
                ("emojis", models.JSONField(default=list)),
                ("card", models.JSONField(blank=True, null=True)),
                ("poll", models.JSONField(blank=True, null=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
                ("reblog", models.TextField(blank=True, null=True)),
            ],
            options={
                "unique_together": {("post_id", "account")},
            },
        ),
    ]
