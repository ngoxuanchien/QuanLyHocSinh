from django.db import models

# Create your models here.
class SchoolClass (models.Model):
    classID = models.CharField(max_length=10, null=False, unique=False)
    n_students = models.IntegerField(null=False)
    school_year = models.CharField(max_length=200, unique=True)

    def __str__ (self):
        return self.classID