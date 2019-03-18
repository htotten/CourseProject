from django.shortcuts import render

from add_courses.models import CourseEnroll
from course_project.models import CourseData


def create_course_sched(request):
    if request.method=="POST":
        course_ids = request.POST.getlist("select-courses")
        semester = request.POST.get("select-semester")
        user = request.user
        courses_qs = CourseData.objects.filter(pk__in=course_ids)  #qs == query set

        if semester=="yr1-sem1":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr1_sem1=True)

        elif semester=="yr1-sem2":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr1_sem2=True)

        elif semester=="yr2-sem1":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr2_sem1=True)

        elif semester=="yr2-sem2":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr2_sem2=True)

        elif semester=="yr3-sem1":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr3_sem1=True)

        elif semester=="yr3-sem2":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr3_sem2=True)

        elif semester=="yr4-sem1":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr4_sem1=True)

        elif semester=="yr4-sem2":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, yr4_sem2=True)

        elif semester=="extra-sem":
            for course in courses_qs:
                CourseEnroll.objects.get_or_create(user=user, course=course, extra_sem=True)


        data1 = CourseEnroll.objects.filter(user=user, yr1_sem1=True)
        data2 = CourseEnroll.objects.filter(user=user, yr1_sem2=True)
        data3 = CourseEnroll.objects.filter(user=user, yr2_sem1=True)
        data4 = CourseEnroll.objects.filter(user=user, yr2_sem2=True)
        data5 = CourseEnroll.objects.filter(user=user, yr3_sem1=True)
        data6 = CourseEnroll.objects.filter(user=user, yr3_sem2=True)
        data7 = CourseEnroll.objects.filter(user=user, yr4_sem1=True)
        data8 = CourseEnroll.objects.filter(user=user, yr4_sem2=True)
        data9 = CourseEnroll.objects.filter(user=user, extra_sem=True)

        course_data = CourseData.objects.all()
        context= {"sem1" : data1,
                  "sem2": data2,
                  "sem3": data3,
                  "sem4": data4,
                  "sem5": data5,
                  "sem6": data6,
                  "sem7": data7,
                  "sem8": data8,
                  "sem9": data9,
                  "course_data" : course_data}
        return render(request, "course_project/my-page.html", context)






