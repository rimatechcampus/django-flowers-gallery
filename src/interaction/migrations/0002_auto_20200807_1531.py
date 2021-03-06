# Generated by Django 3.1 on 2020-08-07 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0002_auto_20200807_1403'),
        ('interaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='flower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='flowers.flower'),
        ),
        migrations.AlterField(
            model_name='action',
            name='liked',
            field=models.BooleanField(null=True),
        ),
    ]
