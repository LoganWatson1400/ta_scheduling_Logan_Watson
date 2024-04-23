from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    # Add other fields as needed

    def __str__(self):
        return self.title


class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.TextField()

    # Add other fields as needed

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.TextField()

    # Add other fields as needed

    def __str__(self):
        return self.user.username


class CourseAssignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ta = models.ForeignKey(TA, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    # Add other fields as needed

    def __str__(self):
        return f"{self.course.title} - {self.ta.user.username}"


class ContactInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} - {self.email}'


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Additional fields can be added here as needed

    def __str__(self):
        return f'{self.course.title} Assignment'
    