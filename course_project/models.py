from django.db import models

# Create your models here.

'''
class CourseData(models.Model):
    course_name = models.CharField(blank=True, null=True, max_length=225)
    course_subject = models.CharField(blank=True, null=True, max_length=225)
    course_num = models.IntegerField(blank=True, null=True)
    course_title = models.CharField(blank=True, null=True, max_length=225)
    course_dept = models.CharField(blank=True, null=True, max_length=225)
    course_creds = models.IntegerField(blank=True, null=True)


    def __str__(self):
        if self.course_title:
            return self.course_title
        else:
            return "No title"

'''



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





























