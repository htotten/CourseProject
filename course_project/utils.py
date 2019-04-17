
import django
django.setup()

import csv
from course_project.models import CourseData




# with open('TempCSV-2.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     x = 0
#     for row in csv_reader:
#         if (x==0 or row[0]==""):
#             x=1
#         else:
#             course_name = row[1]
#             course_subject = row[2]
#             course_num = row[3] #dont forget
#             course_title = row[4]
#             course_dept = row[5]
#             course_creds = row[6]
#
#             CourseData.objects.create(course_name=course_name, course_subject=course_subject,
#                                       course_num=course_num, course_title=course_title,
#                                       course_dept=course_dept, course_creds=course_creds)







with open('https://drive.google.com/file/d/1UeWORIHEIYhsnB0oh1Ep7u9YzAcGs1Ec/view?usp=sharing') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    x = 0
    for row in csv_reader:
        if (x==0):
            x=1
        else:
            course_name = row[1]
            course_subject = row[2]
            course_num = row[3] #dont forget
            course_title = row[4]
            course_dept = row[5]
            course_creds_min = row[6]

            course_creds_max = row[7]
            if(course_creds_max==""):
                course_creds_max = course_creds_min

            course_prereqs = row[8]
            course_locations_1 = row[9]
            course_locations_2 = row[10]
            course_locations_3 = row[11]
            course_types_1 = row[12]
            course_types_2 = row[13]
            course_types_3 = row[14]
            course_types_4 = row[15]
            course_types_5 = row[16]

            CourseData.objects.create(course_name=course_name, course_subject=course_subject,
                                      course_num=course_num, course_title=course_title,
                                      course_dept=course_dept, course_creds_min=course_creds_min,
                                      course_creds_max=course_creds_max, course_prereqs=course_prereqs,
                                      course_locations_1=course_locations_1, course_locations_2=course_locations_2,
                                      course_locations_3=course_locations_3, course_types_1=course_types_1,
                                      course_types_2=course_types_2, course_types_3=course_types_3,
                                      course_types_4=course_types_4, course_types_5=course_types_5)






































