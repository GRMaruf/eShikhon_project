from django.db import models

# Create your models here.
class Trainer(models.Model):
    # Primary Information
    TrainerID = models.CharField(max_length=25)
    Name = models.CharField(max_length=25)
    Designation = models.CharField(max_length=25)

    # Detailed Information
    Age = models.PositiveSmallIntegerField()
    Address = models.CharField(max_length=25)
    HomeDistrict = models.CharField(max_length=25)
    NID = models.CharField(max_length=25)
    
    JoinDate = models.DateField()
    YearOfExperience = models.PositiveSmallIntegerField()
    PreviouslyWorkedIn = models.TextField() # name, designation , duration

    WorkingHours = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    CourseAssigned = models.CharField(max_length=200)
    BatchAssigned = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.Name
    
class Student(models.Model):
    # Primary Information
    StudentID = models.CharField(max_length=25)
    Name = models.CharField(max_length=25)
    CourseEnrolled = models.CharField(max_length=25)
    Batch = models.CharField(max_length=25)

    # Detailed Information
    Age = models.PositiveSmallIntegerField()
    Address = models.CharField(max_length=255)
    HomeDistrict = models.CharField(max_length=25)
    NID = models.CharField(max_length=25)
    
    ProgressStatus = models.CharField(max_length=25)
    PreviousSkills = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Course(models.Model):
    # Primary Information
    CourseID = models.CharField(max_length=25)
    Name = models.CharField(max_length=200)
    Duration = models.CharField(max_length=25)

    # Detailed Information
    Description = models.TextField()
    Syllabus = models.TextField()
    TrainerAssigned = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    
class Co_Worker(models.Model):
    # Primary Information
    WorkerID = models.CharField(max_length=25)
    Name = models.CharField(max_length=25)
    Designation = models.CharField(max_length=25)

    # Detailed Information
    Age = models.PositiveSmallIntegerField()
    Address = models.CharField(max_length=255)
    HomeDistrict = models.CharField(max_length=25)
    NID = models.CharField(max_length=25)
    
    JoinDate = models.DateField()
    YearOfExperience = models.PositiveSmallIntegerField()
    PreviouslyWorkedIn = models.TextField() # name, designation , duration

    WorkingHours = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name