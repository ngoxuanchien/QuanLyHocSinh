import django_filters
from django_filters import CharFilter, ChoiceFilter
from .models import *
from django import forms


class ClassFilter(django_filters.FilterSet):
    # try:
    class_list = []
    year_list = []
    for student in Student.objects.all():
        for c in student.classOfSchool.all():
            class_list.append(c)
            year_list.append(c.year.year)
    class_choices = [(c.classID, c.classID) for c in set(class_list)]
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
    # ''''''

    class Meta:
        model = Student
        fields = []

    def filter_by_class(self, queryset, name, value):
        return queryset.filter(classOfSchool__classID=value)

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(classOfSchool__year=Age.objects.get(year=value))


class MarkFilter(django_filters.FilterSet):
    try:
        years = set([mark.subject.year for mark in Mark.objects.all()])
        year_choices = [(y, y) for y in years]
        year = ChoiceFilter(
            label='Niên khóa',
            choices=year_choices,
            method='filter_by_year',
            widget=forms.Select(attrs={'class': 'form-select'})
        )
        # print(years)

        class_list = []
        for mark in Mark.objects.all():
            for c in mark.student.classOfSchool.filter(year=mark.subject.year):
                class_list.append(c)
        class_choices = [(c.classID, c.classID) for c in set(class_list)]
        # print(class_list)
        classOfSchool = ChoiceFilter(
            label='Lớp',
            choices=class_choices,
            method='filter_by_class',
            widget=forms.Select(attrs={'class': 'form-select'})
        )

        subject_list = set([mark.subject.name for mark in Mark.objects.all()])
        subject_choices = [(s, s) for s in subject_list]
        subject = ChoiceFilter(
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
        fields = ['subject', 'semester_mark', 'year']

    def filter_by_class(self, queryset, name, value):
        return queryset.filter(student__classOfSchool__classID=value)

    def filter_by_subject(self, queryset, name, value):
        return queryset.filter(subject__name=value)

    def filter_by_semester(self, queryset, name, value):
        return queryset.filter(semester_mark=value)

    def filter_by_year(self, queryset, name, value):
        return queryset.filter(subject__year=Age.objects.get(year=value))


class StudentInMarkFilter(django_filters.FilterSet):
    try:
        name = CharFilter(
            field_name='student__user__name',
            label='',
            widget=forms.TextInput(attrs={'class': 'form-control'}),
            lookup_expr='icontains'
        )
    except:
        ''''''
    class Meta:
        model = Mark
        fields = []
