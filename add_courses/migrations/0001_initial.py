# Generated by Django 2.1.7 on 2019-03-12 08:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_project', '0002_auto_20190305_0724'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fresh_first_sem', models.BooleanField(default=False)),
                ('fresh_second_sem', models.BooleanField(default=False)),
                ('soph_first_sem', models.BooleanField(default=False)),
                ('soph_second_sem', models.BooleanField(default=False)),
                ('jun_first_sem', models.BooleanField(default=False)),
                ('jun_second_sem', models.BooleanField(default=False)),
                ('sen_first_sem', models.BooleanField(default=False)),
                ('sen_second_sem', models.BooleanField(default=False)),
                ('extra_sem', models.BooleanField(default=False)),
                ('course', models.ManyToManyField(blank=True, null=True, to='course_project.CourseData')),
                ('user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
