# Generated by Django 4.1.7 on 2023-02-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_alter_customuser_nickname"),
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="accounts.customuser"
            ),
        ),
    ]
