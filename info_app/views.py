from django.utils import timezone

from django.shortcuts import redirect, render
from .models import Trainer, Student, Course, Co_Worker

# Create your views here.
def home(request):
    return render(request, 'home.html')

def trainers(request):
    # Let's fetch the trainers who are added today and pass it to the template
    today_trainers = Trainer.objects.filter(created_at__date=timezone.now().date())

    context = {
        'trainers': Trainer.objects.all(),
        'today_trainers': today_trainers
    }
    return render(request, 'trainers.html', context)

def students(request):
    # Let's fetch the students who are added today and pass it to the template
    today_students = Student.objects.filter(created_at__date=timezone.now().date())

    context = {
        'students': Student.objects.all(),
        'today_students': today_students
    }
    return render(request, 'students.html', context)

def courses(request):
    # Let's fetch the courses who are added today and pass it to the template
    today_courses = Course.objects.filter(created_at__date=timezone.now().date())

    context = {
        'courses': Course.objects.all(),
        'today_courses': today_courses
    }
    return render(request, 'courses.html', context)

def co_workers(request):
    # Let's fetch the co-workers who are added today and pass it to the template
    today_co_workers = Co_Worker.objects.filter(created_at__date=timezone.now().date())

    context = {
        'co_workers': Co_Worker.objects.all(),
        'today_co_workers': today_co_workers
    }
    return render(request, 'co_workers.html', context)

def trainer_detail(request, trainer_id):
    return render(request, 'trainer_detail.html', {'trainer': Trainer.objects.get(id=trainer_id)})

def student_detail(request, student_id):
    # Fetch student details based on student_id
    return render(request, 'student_detail.html', {'student': Student.objects.get(id=student_id)})

def course_detail(request, course_id):  
    # Fetch course details based on course_id
    return render(request, 'course_detail.html', {'course': Course.objects.get(id=course_id)})

def co_worker_detail(request, worker_id):
    # Fetch co-worker details based on worker_id
    return render(request, 'co_worker_detail.html', {'worker': Co_Worker.objects.get(id=worker_id)})

def entry_new_student(request):
    # Logic to handle new student entry
    if request.method == 'POST':
        Name = request.POST.get('Name')
        StudentID = request.POST.get('StudentID')
        CourseEnrolled = request.POST.get('CourseEnrolled')
        Batch = request.POST.get('Batch')
        Age = request.POST.get('Age')
        Address = request.POST.get('Address')
        HomeDistrict = request.POST.get('HomeDistrict')
        NID = request.POST.get('NID')
        ProgressStatus = request.POST.get('ProgressStatus')
        PreviousSkills = request.POST.get('PreviousSkills')

        Student.objects.create(
            Name=Name,
            StudentID=StudentID,
            CourseEnrolled=CourseEnrolled,
            Batch=Batch,
            Age=Age,
            Address=Address,
            HomeDistrict=HomeDistrict,
            NID=NID,
            ProgressStatus=ProgressStatus,
            PreviousSkills=PreviousSkills
        )
        return redirect('students')  # Redirect to the students list after successful entry
    return render(request, 'entry_new_student.html')

def update_student(request, student_id):
    # Logic to handle student information update
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.Name = request.POST.get('Name')
        student.StudentID = request.POST.get('StudentID')
        student.CourseEnrolled = request.POST.get('CourseEnrolled')
        student.Batch = request.POST.get('Batch')
        student.Age = request.POST.get('Age')
        student.Address = request.POST.get('Address')
        student.HomeDistrict = request.POST.get('HomeDistrict')
        student.NID = request.POST.get('NID')
        student.ProgressStatus = request.POST.get('ProgressStatus')
        student.PreviousSkills = request.POST.get('PreviousSkills')
        student.save()
        return redirect('student_detail', student_id=student.id)  # Redirect to the updated student's detail page
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, student_id):
    # Logic to handle student deletion
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students')  # Redirect to the students list after deletion

def entry_new_trainer(request):
    # Logic to handle new trainer entry
    if request.method == 'POST':
        Name = request.POST.get('Name')
        TrainerID = request.POST.get('TrainerID')
        Designation = request.POST.get('Designation')
        CourseAssigned = request.POST.get('CourseAssigned')
        BatchAssigned = request.POST.get('BatchAssigned')
        Age = request.POST.get('Age')
        Address = request.POST.get('Address')
        HomeDistrict = request.POST.get('HomeDistrict')
        NID = request.POST.get('NID')
        JoinDate = request.POST.get('JoinDate')
        YearOfExperience = request.POST.get('YearOfExperience')
        PreviouslyWorkedIn = request.POST.get('PreviouslyWorkedIn')
        WorkingHours = request.POST.get('WorkingHours')
        salary = request.POST.get('salary')

        Trainer.objects.create(
            Name=Name,
            TrainerID=TrainerID,
            Designation=Designation,
            CourseAssigned=CourseAssigned,
            BatchAssigned=BatchAssigned,
            Age=Age,
            Address=Address,
            HomeDistrict=HomeDistrict,
            NID=NID,
            JoinDate=JoinDate,
            YearOfExperience=YearOfExperience,
            PreviouslyWorkedIn=PreviouslyWorkedIn,
            WorkingHours=WorkingHours,
            salary=salary
        )
        return redirect('trainers')  # Redirect to the trainers list after successful entry
    return render(request, 'entry_new_trainer.html')

def update_trainer(request, trainer_id):
    # Logic to handle trainer information update
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        trainer.Name = request.POST.get('Name')
        trainer.TrainerID = request.POST.get('TrainerID')
        trainer.Designation = request.POST.get('Designation')
        trainer.CourseAssigned = request.POST.get('CourseAssigned')
        trainer.BatchAssigned = request.POST.get('BatchAssigned')
        trainer.Age = request.POST.get('Age')
        trainer.Address = request.POST.get('Address')
        trainer.HomeDistrict = request.POST.get('HomeDistrict')
        trainer.NID = request.POST.get('NID')
        trainer.JoinDate = request.POST.get('JoinDate')
        trainer.YearOfExperience = request.POST.get('YearOfExperience')
        trainer.PreviouslyWorkedIn = request.POST.get('PreviouslyWorkedIn')
        trainer.WorkingHours = request.POST.get('WorkingHours')
        trainer.salary = request.POST.get('salary')
        trainer.save()
        return redirect('trainer_detail', trainer_id=trainer.id)  # Redirect to the updated trainer's detail page
    return render(request, 'update_trainer.html', {'trainer': trainer})

def delete_trainer(request, trainer_id):
    # Logic to handle trainer deletion
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('trainers')  # Redirect to the trainers list after deletion

def entry_new_course(request):
    # Logic to handle new course entry
    if request.method == 'POST':
        CourseID = request.POST.get('CourseID')
        Name = request.POST.get('Name')
        Duration = request.POST.get('Duration')
        Description = request.POST.get('Description')
        Syllabus = request.POST.get('Syllabus')
        TrainerAssigned = request.POST.get('TrainerAssigned')

        Course.objects.create(
            CourseID=CourseID,
            Name=Name,
            Duration=Duration,
            Description=Description,
            Syllabus=Syllabus,
            TrainerAssigned=TrainerAssigned
        )
        return redirect('courses')  # Redirect to the courses list after successful entry
    return render(request, 'entry_new_course.html')

def update_course(request, course_id):
    # Logic to handle course information update
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.CourseID = request.POST.get('CourseID')
        course.Name = request.POST.get('Name')
        course.Duration = request.POST.get('Duration')
        course.Description = request.POST.get('Description')
        course.Syllabus = request.POST.get('Syllabus')
        course.TrainerAssigned = request.POST.get('TrainerAssigned')
        course.save()
        return redirect('course_detail', course_id=course.id)  # Redirect to the updated course's detail page
    return render(request, 'update_course.html', {'course': course})

def delete_course(request, course_id):
    # Logic to handle course deletion
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('courses')  # Redirect to the courses list after deletion

def entry_new_co_worker(request):
    if request.method == 'POST':
        WorkerID = request.POST.get('WorkerID')
        Name = request.POST.get('Name')
        Designation = request.POST.get('Designation')
        Age = request.POST.get('Age')
        Address = request.POST.get('Address')
        HomeDistrict = request.POST.get('HomeDistrict')
        NID = request.POST.get('NID')
        JoinDate = request.POST.get('JoinDate')
        YearOfExperience = request.POST.get('YearOfExperience')
        PreviouslyWorkedIn = request.POST.get('PreviouslyWorkedIn')
        WorkingHours = request.POST.get('WorkingHours')
        salary = request.POST.get('salary')

        Co_Worker.objects.create(
            WorkerID=WorkerID,
            Name=Name,
            Designation=Designation,
            Age=Age,
            Address=Address,
            HomeDistrict=HomeDistrict,
            NID=NID,
            JoinDate=JoinDate,
            YearOfExperience=YearOfExperience,
            PreviouslyWorkedIn=PreviouslyWorkedIn,
            WorkingHours=WorkingHours,
            salary=salary
        )
        return redirect('co_workers')  # Redirect to the co-workers list after successful entry
    return render(request, 'entry_new_co_worker.html')

def update_co_worker(request, worker_id):
    co_worker = Co_Worker.objects.get(id=worker_id)
    if request.method == 'POST':
        co_worker.WorkerID = request.POST.get('WorkerID')
        co_worker.Name = request.POST.get('Name')
        co_worker.Designation = request.POST.get('Designation')
        co_worker.Age = request.POST.get('Age')
        co_worker.Address = request.POST.get('Address')
        co_worker.HomeDistrict = request.POST.get('HomeDistrict')
        co_worker.NID = request.POST.get('NID')
        co_worker.JoinDate = request.POST.get('JoinDate')
        co_worker.YearOfExperience = request.POST.get('YearOfExperience')
        co_worker.PreviouslyWorkedIn = request.POST.get('PreviouslyWorkedIn')
        co_worker.WorkingHours = request.POST.get('WorkingHours')
        co_worker.salary = request.POST.get('salary')
        co_worker.save()
        return redirect('co_worker_detail', worker_id=co_worker.id)  # Redirect to the updated co-worker's detail page
    return render(request, 'update_co_worker.html', {'co_worker': co_worker})

def delete_co_worker(request, worker_id):
    co_worker = Co_Worker.objects.get(id=worker_id)
    co_worker.delete()
    return redirect('co_workers')  # Redirect to the co-workers list after deletion