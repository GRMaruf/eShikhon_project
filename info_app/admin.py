from django.contrib import admin
from .models import Trainer, Student, Course, Co_Worker

# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('TrainerID', 'Name', 'Designation')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentID', 'Name', 'CourseEnrolled', 'Batch')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseID', 'Name', 'Duration')

class Co_WorkerAdmin(admin.ModelAdmin):
    list_display = ('WorkerID', 'Name', 'Designation')

admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Co_Worker, Co_WorkerAdmin)