# Generated by Django 5.1.1 on 2024-09-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_evento_link_alter_evento_local'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]