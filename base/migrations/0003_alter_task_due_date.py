# Generated by Django 3.2.3 on 2021-06-01 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
