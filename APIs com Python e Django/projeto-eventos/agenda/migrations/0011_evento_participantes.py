# Generated by Django 5.1.1 on 2024-09-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_alter_evento_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.IntegerField(default=0),
        ),
    ]