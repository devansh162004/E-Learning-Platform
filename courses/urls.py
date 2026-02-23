from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:id>/', views.enroll, name='enroll'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
