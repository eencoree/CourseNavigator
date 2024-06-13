# Generated by Django 5.0.6 on 2024-05-24 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0002_remove_step_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="step",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="step",
                to="courses.step",
            ),
        ),
        migrations.CreateModel(
            name="TaskOption",
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
                ("text", models.CharField(max_length=100)),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="courses.task",
                    ),
                ),
            ],
        ),
    ]
