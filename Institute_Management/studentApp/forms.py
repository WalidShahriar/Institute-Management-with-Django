from django import forms
from studentApp.models import StudentModel
from authApp.models import UserModel
from django.db import transaction

class StudentForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = StudentModel
        fields = '__all__'
        exclude = ['user']

    @transaction.atomic
    def save(self, commit = True):
        user = UserModel.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password='123',
            user_type = 'Student'
        )

        student = super().save(commit=False)
        student.user = user
        if commit:
            student.save()
        return student