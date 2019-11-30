# Generated by Django 2.1 on 2019-11-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191126_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='btech_per',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Name',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='internship',
            new_name='non_technical_skills',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='mtech_per',
            new_name='technical_skills',
        ),
        migrations.RemoveField(
            model_name='post',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='post',
            name='email_id',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='grad_college',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='grad_course',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='grad_percentage',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='grad_specialisation',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='grad_university',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='grad_year_of_passing',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pg_college',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pg_course',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pg_percentage',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pg_specialisation',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pg_university',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pg_year_of_passing',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='x_board',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='x_percentage',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='xii_board',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='xii_percentage',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
