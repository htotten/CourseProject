from django.contrib.auth.models import User
from django.db import models

from CourseProject import settings
from add_courses.models import CourseEnroll
#from course_project.models import CourseData


class CourseRemove(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    course2 = models.ForeignKey(CourseEnroll, null=True, blank=True, on_delete=models.CASCADE)
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
        return "{0}".format(self.course2)
