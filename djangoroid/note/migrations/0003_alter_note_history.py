# Generated by Django 4.1.7 on 2023-02-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("note", "0002_alter_note_canvas_alter_note_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="history",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
