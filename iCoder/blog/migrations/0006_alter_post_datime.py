# Generated by Django 4.0.4 on 2022-05-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_datime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datime',
            field=models.DateTimeField(),
        ),
    ]
