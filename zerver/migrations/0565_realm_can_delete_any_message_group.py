# Generated by Django 5.0.6 on 2024-07-18 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0564_purge_nagios_messages"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="can_delete_any_message_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]