# Generated by Django 5.1.1 on 2024-09-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_rename_user_application_candidate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='full-time', max_length=20),
        ),
    ]
