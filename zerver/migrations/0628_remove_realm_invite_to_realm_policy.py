# Generated by Django 5.0.9 on 2024-11-16 08:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0627_alter_realm_can_invite_users_group"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="invite_to_realm_policy",
        ),
    ]