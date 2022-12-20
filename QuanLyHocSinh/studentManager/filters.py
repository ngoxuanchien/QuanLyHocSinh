import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *
from django import forms


class classFilter(django_filters.FilterSet):
    try:
        classes =[]
        year = []
        for student in Student.objects.all():
            for c in student.classInSchool.all():
                classes.append(c)
                year.append(c.school_year.year)
        class_choices = [(c.classID, c.classID) for c in set(classes)]
        classInSchool = ChoiceFilter(
            label='',
            choices=class_choices,
            method='filter_by_class',
            widget=forms.Select(attrs={'class': 'form-select'})
        )

        year_choices = [(y, y) for y in set(year)]

        year = ChoiceFilter(
            label='Niên khóa',
            choices=year_choices,
            method='filter_by_year',
            widget=forms.Select(attrs={'class': 'form-select'})
        )
    except:
        ''''''

    class Meta:
        model = Student
        fields = []
    
    def filter_by_class(self, queryset, name, value):
        return queryset.filter(classInSchool__classID = value)

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(classInSchool__school_year = Age.objects.get(year = value))