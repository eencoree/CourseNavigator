from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/step/<int:step_id>/', views.step_detail, name='step_detail'),
    path('<int:course_id>/task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:course_id>/content/<int:content_id>/', views.content_detail, name='content_detail'),
    path('student_course/<int:student_course_id>/', views.student_course_detail, name='student_course_detail'),
    path('step_student/<int:step_student_id>/', views.step_student_detail, name='step_student_detail'),

    path('create_course/', views.create_course, name='create_course'),
    path('create_step/<int:course_id>/', views.create_step, name='create_step'),
    path('create_type/<int:step_id>/', views.create_type, name='create_type'),
    path('create_task/<int:step_id>/<int:type_id>/', views.create_task, name='create_task'),

    path('step/<int:step_id>/', views.step_detail, name='step_detail'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
]
