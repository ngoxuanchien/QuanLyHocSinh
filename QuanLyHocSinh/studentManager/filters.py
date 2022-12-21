import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *
from django import forms

class ClassFilter(django_filters.FilterSet):
    try:
        class_list =[]
        year_list = []
        for student in Student.objects.all():
            for c in student.classOfSchool.all():
                class_list.append(c)
                year_list.append(c.year.year)
        class_choices = [(c.classID, c.classID) for c in set(class_list)]
        classInSchool = ChoiceFilter(
            label='',
            choices=class_choices,
            method='filter_by_class',
            widget=forms.Select(attrs={'class': 'form-select'})
        )

        year_choices = [(y, y) for y in set(year_list)]

        year_list = ChoiceFilter(
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
        return queryset.filter(classOfSchool__classID = value)

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(classOfSchool__year = Age.objects.get(year_list = value))