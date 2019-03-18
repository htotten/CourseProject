from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(template_name='signup/signup.html'), name='signup')
]