from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from course_project.models import CourseData
from course_project.models import CourseEnroll


def my_first_view(request):

    course_subjects = ["All",
                       "AN", "APP", "ART", "BIO", "CHM", "COM", "CS", "EB", "ED", "ENG",
                       "ENV", "FR", "GER", "GRK", "HB", "HIS", "IS", "KNS", "LS", "MA",
                       "MU", "MUA", "OCP", "PEA", "PHI", "PHS", "PHY", "POL", "PSY", "RS",
                       "SOC", "SP", "TA"]
    course_subj = "All"
    course_data = CourseData.objects.all()

    if request.method == "GET":


        # ---------------------------------------------------------------------------------#
        # ---------------------------- STARTUP --------------------------------------------#
        # ---------------------------------------------------------------------------------#
        user = request.user
        user_courses = CourseEnroll.objects.filter(user=user)
#        course_depts = ["All", "BS",  "HIS", "IS",  "POL", "ML",  "KNS", "APP",
#                        "EB",  "ENG", "PHI", "COM", "BIO", "MA", "TA", "CS",
#                        "PHY", "PSY", "CHM", "SOC", "ART", "MU", "ED"]
#        course_dept = "All"
        data1 = CourseEnroll.objects.filter(user=user, yr1_sem1=True)
        data2 = CourseEnroll.objects.filter(user=user, yr1_sem2=True)
        data3 = CourseEnroll.objects.filter(user=user, yr2_sem1=True)
        data4 = CourseEnroll.objects.filter(user=user, yr2_sem2=True)
        data5 = CourseEnroll.objects.filter(user=user, yr3_sem1=True)
        data6 = CourseEnroll.objects.filter(user=user, yr3_sem2=True)
        data7 = CourseEnroll.objects.filter(user=user, yr4_sem1=True)
        data8 = CourseEnroll.objects.filter(user=user, yr4_sem2=True)
        data9 = CourseEnroll.objects.filter(user=user, extra_sem=True)
        context = {"sem1": data1,
                   "sem2": data2,
                   "sem3": data3,
                   "sem4": data4,
                   "sem5": data5,
                   "sem6": data6,
                   "sem7": data7,
                   "sem8": data8,
                   "sem9": data9,
                   "enrolled_courses": user_courses,
                   "course_data": course_data,
                   "course_subjects": course_subjects,
                   "course_subj": course_subj}
        return render(request, "course_project/my-page.html", context)

    elif request.method == "POST":

        # ---------------------------------------------------------------------------------#
        # ---------------------------- ADDING COURSE(S) -----------------------------------#
        # ---------------------------------------------------------------------------------#
        if request.POST.keys().__contains__("add-button"):
            user = request.user
            user_courses = CourseEnroll.objects.filter(user=user)

            course_ids = request.POST.getlist("select-courses")
            semester = request.POST.get("select-semester")
#            course_depts = ["All", "BS", "HIS", "IS", "POL", "ML", "KNS", "APP",
#                            "EB", "ENG", "PHI", "COM", "BIO", "MA", "TA", "CS",
#                            "PHY", "PSY", "CHM", "SOC", "ART", "MU", "ED"]
            courses_qs = CourseData.objects.filter(pk__in=course_ids)
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
            context= {"sem1" : data1,
                      "sem2": data2,
                      "sem3": data3,
                      "sem4": data4,
                      "sem5": data5,
                      "sem6": data6,
                      "sem7": data7,
                      "sem8": data8,
                      "sem9": data9,
                      "enrolled_courses": user_courses,
                      "course_data": course_data,
                      "course_subjects": course_subjects,
                      "course_subj": course_subj}
            return render(request, "course_project/my-page.html", context)

        #---------------------------------------------------------------------------------#
        #---------------------------- SELECTED DEPARTMENT --------------------------------#
        #---------------------------------------------------------------------------------#
        elif request.POST.keys().__contains__("subj-button"):
            print(request.POST)

            user = request.user
            user_courses = CourseEnroll.objects.filter(user=user)
            course_subj = request.POST.get("select-subj")
            if course_subj != "All":
                course_data = CourseData.objects.filter(course_subject=course_subj)  # qs == query set
            else:
                course_data = CourseData.objects.all()
#            course_depts = ["All", "BS", "HIS", "IS", "POL", "ML", "KNS", "APP",
#                            "EB", "ENG", "PHI", "COM", "BIO", "MA", "TA", "CS",
#                            "PHY", "PSY", "CHM", "SOC", "ART", "MU", "ED"]
            data1 = CourseEnroll.objects.filter(user=user, yr1_sem1=True)
            data2 = CourseEnroll.objects.filter(user=user, yr1_sem2=True)
            data3 = CourseEnroll.objects.filter(user=user, yr2_sem1=True)
            data4 = CourseEnroll.objects.filter(user=user, yr2_sem2=True)
            data5 = CourseEnroll.objects.filter(user=user, yr3_sem1=True)
            data6 = CourseEnroll.objects.filter(user=user, yr3_sem2=True)
            data7 = CourseEnroll.objects.filter(user=user, yr4_sem1=True)
            data8 = CourseEnroll.objects.filter(user=user, yr4_sem2=True)
            data9 = CourseEnroll.objects.filter(user=user, extra_sem=True)
            context = {"sem1": data1,
                       "sem2": data2,
                       "sem3": data3,
                       "sem4": data4,
                       "sem5": data5,
                       "sem6": data6,
                       "sem7": data7,
                       "sem8": data8,
                       "sem9": data9,
                       "enrolled_courses": user_courses,
                       "course_data": course_data,
                       "course_subjects": course_subjects,
                       "course_subj": course_subj}
            return render(request, "course_project/my-page.html", context)


        # ---------------------------------------------------------------------------------#
        # ---------------------------- DELETING COURSE(S) ---------------------------------#
        # ---------------------------------------------------------------------------------#
        elif request.POST.keys().__contains__("delete-button"):
            user = request.user
            user_courses = CourseEnroll.objects.filter(user=user)
            course_ids = request.POST.getlist("select-courses2")
            courses_qs = CourseEnroll.objects.filter(pk__in=course_ids)
#            course_depts = ["All", "BS", "HIS", "IS", "POL", "ML", "KNS", "APP",
#                            "EB", "ENG", "PHI", "COM", "BIO", "MA", "TA", "CS",
#                            "PHY", "PSY", "CHM", "SOC", "ART", "MU", "ED"]
            for course in courses_qs:
                route = get_object_or_404(CourseEnroll, pk=course.pk)
                route.delete()
            data1 = CourseEnroll.objects.filter(user=user, yr1_sem1=True)
            data2 = CourseEnroll.objects.filter(user=user, yr1_sem2=True)
            data3 = CourseEnroll.objects.filter(user=user, yr2_sem1=True)
            data4 = CourseEnroll.objects.filter(user=user, yr2_sem2=True)
            data5 = CourseEnroll.objects.filter(user=user, yr3_sem1=True)
            data6 = CourseEnroll.objects.filter(user=user, yr3_sem2=True)
            data7 = CourseEnroll.objects.filter(user=user, yr4_sem1=True)
            data8 = CourseEnroll.objects.filter(user=user, yr4_sem2=True)
            data9 = CourseEnroll.objects.filter(user=user, extra_sem=True)
            context = {"sem1": data1,
                       "sem2": data2,
                       "sem3": data3,
                       "sem4": data4,
                       "sem5": data5,
                       "sem6": data6,
                       "sem7": data7,
                       "sem8": data8,
                       "sem9": data9,
                       "enrolled_courses": user_courses,
                       "course_data": course_data,
                       "course_subjects": course_subjects,
                       "course_subj": course_subj}
            return render(request, "course_project/my-page.html", context)





