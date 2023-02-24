# Generated by Django 4.1.7 on 2023-02-24 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("note", "0002_rename_create_at_note_created_at_and_more"),
        ("comment", "0002_alter_comment_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="note",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="note.note"
            ),
        ),
    ]