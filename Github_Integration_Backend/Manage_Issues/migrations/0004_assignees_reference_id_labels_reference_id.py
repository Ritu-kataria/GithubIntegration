# Generated by Django 4.0.4 on 2022-05-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage_Issues', '0003_remove_assignees_reference_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignees',
            name='reference_id',
            field=models.IntegerField(default=None, verbose_name='Reference ID'),
        ),
        migrations.AddField(
            model_name='labels',
            name='reference_id',
            field=models.IntegerField(default=None, verbose_name='Reference ID'),
        ),
    ]
