from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from course_project.models import CourseData
from add_courses.models import CourseEnroll


def my_first_view(request):
    course_depts = ["All", "RS", "HIS", "IS", "POL", "ML", "KNS", "APP",
                    "EB", "ENG", "PHI", "COM", "BIO", "MA", "TA",
                    "PHY", "PSY", "CHM", "SOC", "ART", "MU", "ED"]
    course_dept = "All"
    course_data = CourseData.objects.all()
    user = request.user
    data = CourseEnroll.objects.filter(user=user)
    context = {"enrolled_courses": data, "course_data": course_data,
               "course_depts": course_depts, "course_dept": course_dept}
    return render(request, "course_project/my-page.html", context)





