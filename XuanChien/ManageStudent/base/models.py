from django.db import models
from datetime import datetime

# Create your models here.


class Age(models.Model):
    year = models.CharField(max_length=200, unique=True)
    max_age = models.IntegerField(null=False)
    min_age = models.IntegerField(null=False)

    def __str__(self):
        return self.year


class ClassOfSchool(models.Model):
    classId = models.CharField(max_length=10, null=False, unique=False)
    max_number = models.IntegerField(null=False)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.year.year + '_' + self.classId


class Student(models.Model):
    SEX_CATELOGY = [("1", "Nam"), ("0", "Nữ")]
    # now = datetime.now().strftime('%Y-%m-%d')
    name = models.CharField(max_length=100)
    dateOfBirth = models.DateField(null=True)
    # default=datetime.strptime(now, '%Y-%m-%d'))
    sex = models.CharField(default='1', choices=SEX_CATELOGY, max_length=1)
    address = models.TextField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    classOfSchool = models.ForeignKey(
        ClassOfSchool, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    # SubjectID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False)
    approved_mark = models.FloatField(null=False, default=5.0)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.year.year + '_' + self.name


class Mark(models.Model):
    SEMESTER_CATEGORY = (
        ('1', '1'),
        ('2', '2')
    )
    subjects = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    markFifteen = models.FloatField(null=True, blank=True)
    markOne = models.FloatField(null=True, blank=True)
    markFinal = models.FloatField(null=True, blank=True)
    semester_mark = models.CharField(
        max_length=200, null=False, choices=SEMESTER_CATEGORY)

    def __str__(self):
        return self.student.name + '_' + self.semester_mark
