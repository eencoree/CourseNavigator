# Generated by Django 5.0.6 on 2024-05-24 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0003_task_step_taskoption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="step",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="step",
                to="courses.step",
            ),
        ),
    ]
