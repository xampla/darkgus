# Generated by Django 4.1.7 on 2023-03-22 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dork",
            fields=[
                ("dork", models.TextField(primary_key=True, serialize=False)),
                ("category", models.TextField(blank=True, null=True)),
                ("total_results", models.IntegerField(blank=True, null=True)),
                ("results_gathered", models.IntegerField(blank=True, null=True)),
                ("last_executed", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Result",
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
                ("url", models.TextField()),
                ("description", models.TextField(blank=True, null=True)),
                ("all_info", models.TextField(blank=True, null=True)),
                ("last_detected", models.DateField(blank=True, null=True)),
                (
                    "dork",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="argusdorker.dork",
                    ),
                ),
            ],
            options={
                "unique_together": {("url", "dork")},
            },
        ),
    ]
