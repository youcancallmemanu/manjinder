# Generated by Django 4.0.4 on 2022-05-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datime',
            field=models.DateTimeField(blank=True),
        ),
    ]
