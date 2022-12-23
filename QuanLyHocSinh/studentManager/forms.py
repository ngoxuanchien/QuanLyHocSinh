from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, CharField, Select

class YearForm(ModelForm):
    try:
        year_choices = set([(a, a.year) for a in Age.objects.all()])
        year = CharField(label="",widget=Select(
            choices=year_choices, 
            attrs={'class': 'form-select'
        }))
    except:
        ''''''
    class Meta:
        model = Age
        fields = ['year']


class lapDSForm(ModelForm):
    def __init__(self, *args,**kwargs):
        self.pk = kwargs.pop('pk', None)
        super(lapDSForm,self).__init__(*args,**kwargs)
        age = Age.objects.get(id = self.pk)
        class_choices = set([(c.classID, c.classID) for c in SchoolClass.objects.filter(year = age)])
        self.fields['classId'].label = ''
        self.fields['classId'].widget = Select(
            choices=class_choices, 
            attrs={'class': 'form-select'}
        )

    class Meta:
        model = SchoolClass
        fields = ['classID']