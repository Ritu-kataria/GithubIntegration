# Generated by Django 4.0.4 on 2022-05-10 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manage_Issues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issues',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='issues',
            name='label',
        ),
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_id', models.IntegerField(db_index=True, unique=True, verbose_name='Label ID')),
                ('reference_id', models.IntegerField(unique=True, verbose_name='Reference ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='Description')),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_labels', to='Manage_Issues.issues')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
            },
        ),
        migrations.CreateModel(
            name='Assignees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee_id', models.IntegerField(db_index=True, unique=True, verbose_name='Assignee ID')),
                ('reference_id', models.IntegerField(unique=True, verbose_name='Reference ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignees', to='Manage_Issues.issues')),
            ],
            options={
                'verbose_name': 'Assignee',
                'verbose_name_plural': 'Assignees',
            },
        ),
    ]
