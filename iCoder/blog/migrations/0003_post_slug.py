# Generated by Django 4.0.4 on 2022-05-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_contact_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
