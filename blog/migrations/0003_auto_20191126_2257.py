# Generated by Django 2.1 on 2019-11-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191126_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tile',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='asd',
            new_name='btech_per',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='internship',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='mtech_per',
            field=models.TextField(default='yoyoyo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='phone_no',
            field=models.TextField(default='123123'),
            preserve_default=False,
        ),
    ]
