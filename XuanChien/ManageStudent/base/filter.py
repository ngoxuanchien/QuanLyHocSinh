import django_filters
from django_filters import ChoiceFilter
from .models import *
from django import forms


class ClassFilter(django_filters.FilterSet):
    # try:
    class_list = []
    year_list = []
    for student in Student.objects.all():
        c = student.classOfSchool
        class_list.append(c)
        year_list.append(c.year.year)
    class_choices = [(c.classId, c.classId) for c in set(class_list)]
    classOfSchool = ChoiceFilter(
        label='',
        choices=class_choices,
        method='filter_by_class',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    year_choices = [(y, y) for y in set(year_list)]

    year = ChoiceFilter(
        label='Niên khóa',
        choices=year_choices,
        method='filter_by_year',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # except:
    #     ''''''

    class Meta:
        model = Student
        fields = []

    def filter_by_class(self, queryset, name, value):
        return queryset.filter(classOfSchool__classId=value)

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(classOfSchool__year=Age.objects.get(year=value))


class YearFilter(django_filters.FilterSet):
    try:
        years = set([c.year.year for c in ClassOfSchool.objects.all()])
        year = ChoiceFilter(
            label='',
            choices=[(c, c) for c in years],
            method='filter_by_year',
            widget=forms.Select(attrs={'class': 'form-select'})
        )
    except:
        ''''''
    class Meta:
        model = Student
        fields = []

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(year__year=value)


class MarkFilter(django_filters.FilterSet):
    try:
        years = set([mark.subjects.year for mark in Mark.objects.all()])
        year_choices = [(y, y) for y in years]
        year = ChoiceFilter(
            label='Năm học',
            choices=year_choices,
            method='filter_by_year',
            widget=forms.Select(attrs={'class': 'form-select'})
        )

        class_list = []
        for mark in Mark.objects.all():
            class_list.append(mark.student.classOfSchool)
        class_choices = [(c.classId, c.classId) for c in set(class_list)]
        classOfSchool = ChoiceFilter(
            label='Lớp',
            choices=class_choices,
            method='filter_by_class',
            widget=forms.Select(attrs={'class': 'form-select'})
        )

        subject_list = set([mark.subject.name for mark in Mark.objects.all()])
        subject_choices = [(s, s) for s in subject_list]
        subjects = ChoiceFilter(
            label='Môn học',
            choices=subject_choices,
            method='filter_by_subject',
            widget=forms.Select(attrs={'class': 'form-select'})
        )
        SEMESTER_CATEGORY = (
            ('1', '1'),
            ('2', '2')
        )
        semester_mark = ChoiceFilter(
            label='Học kì',
            choices=SEMESTER_CATEGORY,
            method='filter_by_semester',
            widget=forms.Select(attrs={'class': 'form-select'})
        )
    except:
        ''''''
    class Meta:
        model = Mark
        fields = ['subjects', 'semester_mark']

    def filter_by_class(self, queryset, name, value):
        return queryset.filter(student__classOfSchool__classId=value)

    def filter_by_subject(self, queryset, name, value):
        return queryset.filter(subjects__name=value)

    def filter_by_semester(self, queryset, name, value):
        return queryset.filter(semester_mark=value)

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(subject__year=Age.objects.get(year=value))
