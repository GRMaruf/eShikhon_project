from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trainers/', views.trainers, name='trainers'),
    path('students/', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('co-workers/', views.co_workers, name='co_workers'),
    path('trainer/<int:trainer_id>/', views.trainer_detail, name='trainer_detail'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('co-worker/<int:worker_id>/', views.co_worker_detail, name='co_worker_detail'),
    path('entry-new-student/', views.entry_new_student, name='entry_new_student'),
    path('update-student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('entry-new-trainer/', views.entry_new_trainer, name='entry_new_trainer'),
    path('update-trainer/<int:trainer_id>/', views.update_trainer, name='update_trainer'),
    path('delete-trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('entry-new-course/', views.entry_new_course, name='entry_new_course'), 
    path('update-course/<int:course_id>/', views.update_course, name='update_course'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('entry-new-co-worker/', views.entry_new_co_worker, name='entry_new_co_worker'),
    path('update-co-worker/<int:worker_id>/', views.update_co_worker, name='update_co_worker'),
    path('delete-co-worker/<int:worker_id>/', views.delete_co_worker, name='delete_co_worker'),
]