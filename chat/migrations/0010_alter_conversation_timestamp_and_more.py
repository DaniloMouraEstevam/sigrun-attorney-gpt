# Generated by Django 5.0.1 on 2024-01-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_remove_historyquestion_is_first_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='historyquestion',
            name='date_only',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='historyquestion',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
