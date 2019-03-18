# Generated by Django 2.1.7 on 2019-03-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_project', '0003_auto_20190316_0643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursedata',
            old_name='course_creds',
            new_name='course_creds_min',
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_creds_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_locations_1',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_locations_2',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_locations_3',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_prereqs',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_types_1',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_types_2',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_types_3',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_types_4',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='coursedata',
            name='course_types_5',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
