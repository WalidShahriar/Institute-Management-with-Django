from django import forms
from teacherApp.models import TeacherModel
from authApp.models import UserModel
from django.db import transaction

class TeacherForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = TeacherModel
        fields = '__all__'
        exclude = ['user']

    @transaction.atomic
    def save(self, commit = True):
        user = UserModel.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='123',
            user_type = 'Teacher'
        )

        teacher = super().save(commit=False)
        teacher.user = user
        if commit:
            teacher.save()
        return teacher
