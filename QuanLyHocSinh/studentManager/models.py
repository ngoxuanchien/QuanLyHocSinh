from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser
# Create your models here.
from django.contrib.auth.hashers import make_password
from datetime import datetime, date
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        user = CustomUser(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = (('1', "Admin"), ('2', "Teacher"), ('3', "Student"))
    SEX_CATELOGY = [("1", "Nam"), ("0", "Nữ")]
    # now = datetime.now().strftime('%Y-%m-%d')
    # dateOfBirth = models.DateField(default=datetime.strptime(now,'%Y-%m-%d')
    now = date.today
    username = models.CharField(max_length=200, unique=True)
    role = models.CharField(default='1', choices=USER_TYPE, max_length=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(default='', max_length=200)

    dateOfBirth = models.DateField(default=now)
    sex = models.CharField(default='1', choices=SEX_CATELOGY, max_length=1)
    phone = models.CharField(default='', max_length=20, blank=True)
    email = models.EmailField(max_length=200, unique=True)
    address = models.TextField(default='', blank=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'], name="unique_user")
        ]

    def __str__(self):
        return self.username


class Age(models.Model):
    year = models.CharField(max_length=200, unique=True)
    max_age = models.IntegerField(null=False)
    min_age = models.IntegerField(null=False)

    def __str__(self):
        return self.year


class SchoolClass(models.Model):
    classID = models.CharField(max_length=10, null=False, unique=False)
    n_students = models.IntegerField(null=False)
    year = models.ForeignKey(
        Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.year.year + '_' + self.classID


class Subject(models.Model):
    SubjectID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    approved_mark = models.FloatField(null=False)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    classOfSchool = models.ManyToManyField(SchoolClass, blank=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # classOfSchool = models.ManyToManyField(SchoolClass,blank =True)
    subject = models.ForeignKey(Subject, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Mark(models.Model):
    SEMESTER_CATEGORY = (
        ('1', '1'),
        ('2', '2')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester_mark = models.CharField(
        max_length=200, null=False, choices=SEMESTER_CATEGORY)
    markFifteen = models.FloatField(null=True, blank=True)
    markOne = models.FloatField(null=True, blank=True)
    markFinal = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.student.user.username + '_' + self.semester_mark


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 1:
            Admin.objects.create(admin=instance)
        if instance.role == 2:
            Teacher.objects.create(admin=instance)
        if instance.role == 3:
            Student.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 1:
        instance.admin.save()
    if instance.role == 2:
        instance.teacher.save()
    if instance.role == 3:
        instance.student.save()
