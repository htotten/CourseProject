from django.shortcuts import render

from add_courses.models import CourseEnroll
from course_project.models import CourseData


def courses_by_dept(request):

    if request.method=="POST":
        course_dept = request.POST.getlist("select-dept")
        user = request.user
        courses_qs = CourseData.objects.filter(course_dept=course_dept)

        course_depts = ["All", "RS", "HIS", "IS", "POL", "ML", "KNS", "APP",
                        "EB", "ENG", "PHI", "COM", "BIO", "MA", "TA",
                        "PHY", "PSY", "CHM", "SOC", "ART", "MU", "ED"]
        course_data = CourseData.objects.all()
        user = request.user
        data = CourseEnroll.objects.filter(user=user)
        context = {"enrolled_courses": data, "course_data": course_data,
                   "course_depts": course_depts, "course_dept":course_dept}
        return render(request, "course_project/my-page.html", context)

