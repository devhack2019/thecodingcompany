# Generated by Django 2.1.2 on 2019-01-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20190113_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='classes_held',
            field=models.IntegerField(default=0),
        ),
    ]
