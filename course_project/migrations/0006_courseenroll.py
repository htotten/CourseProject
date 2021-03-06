# Generated by Django 2.1.7 on 2019-03-23 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_project', '0005_auto_20190318_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yr1_sem1', models.BooleanField(default=False)),
                ('yr1_sem2', models.BooleanField(default=False)),
                ('yr2_sem1', models.BooleanField(default=False)),
                ('yr2_sem2', models.BooleanField(default=False)),
                ('yr3_sem1', models.BooleanField(default=False)),
                ('yr3_sem2', models.BooleanField(default=False)),
                ('yr4_sem1', models.BooleanField(default=False)),
                ('yr4_sem2', models.BooleanField(default=False)),
                ('extra_sem', models.BooleanField(default=False)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course_project.CourseData')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
