# Generated by Django 4.2.5 on 2023-09-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_listitem_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='done',
        ),
        migrations.AddField(
            model_name='listitem',
            name='status',
            field=models.TextField(max_length=10, null=True),
        ),
    ]