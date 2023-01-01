from django.forms import ModelForm
from .models import *
from django import forms


class StudentForm(forms.ModelForm):
    dateOfBirth = forms.CharField(label="", widget=forms.DateInput(
        attrs={
            'type': 'date',
            'id': "datepicker",
            'class': 'form-control'
        }))

    class Meta:
        model = Student
        fields = '__all__'


class StudentTemp:
    def __init__(self, id, stt, name, classID, TBHK1, TBHK2):
        self.id = id
        self.stt = stt
        self.name = name
        self.classID = classID
        self.TBHK1 = TBHK1
        self.TBHK2 = TBHK2


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'

# class ClassOfSchool(ModelForm):
#     class Meta:
#         model = ClassOfSchool
#         fields = '__all__'
