from django.db import models
from student.models import Student

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class Option(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, blank=True, null=True)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.value


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='question_images', blank=True, null=True)  # Added photo field
    question_text = models.CharField(max_length=600)
   
    options = models.ManyToManyField(Option, related_name='questions')
    answer = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='correct_answer')

    def __str__(self):
        return self.question_text

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
