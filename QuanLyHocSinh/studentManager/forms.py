from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, CharField, Select
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        


class CustomUserForm(forms.ModelForm):
    try:
        username = forms.CharField(label="", widget=forms.TextInput(
            attrs={'id': "username_user", 'class': "form-control", 'placeholder': 'Username...'
                   }))

        password = forms.CharField(label="", widget=forms.TextInput(
            attrs={'id': "password_user", 'class': "form-control", 'placeholder': 'Password...'
                   }))

        name = forms.CharField(label='', widget=forms.TextInput(
            attrs={'id': "name_user", 'class': "form-control", 'placeholder': 'Họ tên...'
                   }))
        dateOfBirth = forms.CharField(label="", widget=forms.DateInput(
            attrs={'type': 'date', 'id': "datepicker", 'class': 'form-control'
                   }))

        sex = forms.CharField(label="", widget=forms.Select(
            choices=CustomUser().SEX_CATELOGY,
            attrs={'class': 'form-select', 'id': 'sex_user'
                   }))

        email = forms.CharField(label="", widget=forms.TextInput(
            attrs={'type': 'email', 'id': 'email_user', 'class': 'form-control', 'placeholder': 'Email...'
                   }))

        address = forms.CharField(label="", required=False, widget=forms.Textarea(
            attrs={"rows": 2, 'class': 'form-control', 'id': 'address_user',
                   'placeholder': "Địa chỉ"
                   }))
        address.required = False
        
    except:
        ''''''
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserForm, self).__init__(*args, **kwargs)
    #     if kwargs.get('instance'):
    #         instance = kwargs.get('instance').admin.__dict__
    #         self.fields['password'].required = False
    #         for field in CustomUserForm.Meta.fields:
    #             self.fields[field].initial = instance.get(field)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'name',
                  'dateOfBirth', 'sex', 'email', 'address']


class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Admin
        fields = CustomUserForm.Meta.fields


class TeacherForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False
        #self.fields['classOfSchool'].required = False
        #self.fields['subject'].widget.attrs.update({'class': 'form-select'})
        #self.fields['classOfSchool'].widget.attrs.update(            {'class': 'form-select'})

    class Meta:
        model = Teacher
        fields = CustomUserForm.Meta.fields + ['subject']


class StudentForm(CustomUserForm):
    try:
        class_choices = {(None, '-----')}
        class_choices.update(set([(c.classID, c.classID)
                             for c in SchoolClass.objects.all()]))
        classOfSchool = forms.CharField(label="", widget=forms.Select(
            choices=class_choices,
            attrs={'class': 'form-select'
                   }), required=False)
    except:
        ''''''

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['classOfSchool'].required = False
        self.fields['classOfSchool'].widget.attrs.update(
            {'class': 'form-select'})

    class Meta:
        model = Student
        fields = CustomUserForm.Meta.fields + ['classOfSchool']
        # widgets = {
        #     'classOfSchool': forms.Select()
        # }


class updateCustomUserForm(forms.ModelForm):
    try:
        username = forms.CharField(label="", widget=forms.TextInput(
            attrs={'id': "username_user", 'class': "form-control"
                   }))

        name = forms.CharField(label='', widget=forms.TextInput(
            attrs={'id': "name_user", 'class': "form-control"
                   }))
        dateOfBirth = forms.CharField(label="", widget=forms.DateInput(
            attrs={'type': 'date', 'id': "datepicker", 'class': 'form-control'
                   }))

        sex = forms.CharField(label="", widget=forms.Select(
            choices=CustomUser().SEX_CATELOGY,
            attrs={'class': 'form-select', 'id': 'sex_user'
                   }))

        email = forms.CharField(label="", widget=forms.TextInput(
            attrs={'type': 'email', 'id': 'email_user', 'class': 'form-control',
                   }))

        address = forms.CharField(label="", widget=forms.Textarea(
            attrs={"rows": 4, 'class': 'form-control', 'id': 'address_user',
                   }))

        address.required = False
        email.required = True
    except:
        ''''''
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'dateOfBirth',
                  'sex', 'email', 'address']


# class userUpdateForm(forms.ModelForm):
#     try:
#         name = forms.CharField(label='', widget=forms.TextInput(
#             attrs={'id': "name_user", 'class': "form-control"
#                    }))
#         dateOfBirth = forms.CharField(label="", widget=forms.DateInput(
#             attrs={'type': 'date', 'id': "datepicker", 'class': 'form-control'
#                    }))

#         sex = forms.CharField(label="", widget=forms.Select(
#             choices=CustomUser().SEX_CATELOGY,
#             attrs={'class': 'form-select', 'id': 'sex_user'
#                    }))

#         email = forms.CharField(label="", widget=forms.TextInput(
#             attrs={'type': 'email', 'id': 'email_user', 'class': 'form-control',
#                    }))

#         address = forms.CharField(label="", widget=forms.Textarea(
#             attrs={"rows": 4, 'class': 'form-control', 'id': 'address_user',
#                    'placeholder': "12, đường 01, quận 1, tp HCM"
#                    }))

#         phone = forms.CharField(label="", widget=forms.TextInput(
#             attrs={'id': 'phone_user', 'class': 'form-control',
#                    }))
#     except:
#         ''''''
#     class Meta:
#         model = CustomUser
#         fields = ('name', 'dateOfBirth', 'sex', 'phone', 'email', 'address')

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