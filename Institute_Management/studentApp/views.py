from django.shortcuts import render, redirect
from studentApp.models import StudentModel
from studentApp.forms import StudentForm
from django.contrib import messages


def display_student(request):
    student_list = StudentModel.objects.all()

    context = {
        'student_list' : student_list
    }

    return render(request, 'display_student.html', context)

def add_student(request):

    form_data = StudentForm()

    if request.method == 'POST':
        form_data = StudentForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Student Registered Successfully!')
            return redirect('display_student')

    context = {
        'title' : 'Register Student',
        'page_title' : 'Add Student Information',
        'form_data' : form_data,
        'submit_btn_name' : 'Add Student',
        'cancel_btn_name' : 'Discard',
        'cancel_btn_url' : 'display_student',
    }

    return render(request, 'master/base_form.html', context)