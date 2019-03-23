from django.db import models
from django.contrib.auth.models import User


class CourseData(models.Model):
    course_name = models.CharField(blank=True, null=True, max_length=225)
    course_subject = models.CharField(blank=True, null=True, max_length=225)
    course_num = models.CharField(blank=True, null=True, max_length=225)
    course_title = models.CharField(blank=True, null=True, max_length=225)
    course_dept = models.CharField(blank=True, null=True, max_length=225)
    course_creds_min = models.IntegerField(blank=True, null=True)

    course_creds_max = models.IntegerField(blank=True, null=True)
    course_prereqs = models.CharField(blank=True, null=True, max_length=225)
    course_locations_1 = models.CharField(blank=True, null=True, max_length=225)
    course_locations_2 = models.CharField(blank=True, null=True, max_length=225)
    course_locations_3 = models.CharField(blank=True, null=True, max_length=225)
    course_types_1 = models.CharField(blank=True, null=True, max_length=225)
    course_types_2 = models.CharField(blank=True, null=True, max_length=225)
    course_types_3 = models.CharField(blank=True, null=True, max_length=225)
    course_types_4 = models.CharField(blank=True, null=True, max_length=225)
    course_types_5 = models.CharField(blank=True, null=True, max_length=225)

    def __str__(self):
        if self.course_title:
            return self.course_title
        else:
            return "No title"


class CourseEnroll(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseData, null=True, blank=True, on_delete=models.CASCADE)
    yr1_sem1 = models.BooleanField(default=False)
    yr1_sem2 = models.BooleanField(default=False)
    yr2_sem1 = models.BooleanField(default=False)
    yr2_sem2 = models.BooleanField(default=False)
    yr3_sem1 = models.BooleanField(default=False)
    yr3_sem2 = models.BooleanField(default=False)
    yr4_sem1 = models.BooleanField(default=False)
    yr4_sem2 = models.BooleanField(default=False)
    extra_sem = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.course)





























