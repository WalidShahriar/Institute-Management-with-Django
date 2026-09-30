from django.shortcuts import render, redirect
from teacherApp.models import TeacherModel
from teacherApp.forms import TeacherForm
from django.contrib import messages


def display_teacher(request):
    teacher_list = TeacherModel.objects.all()

    context = {
        'teacher_list' : teacher_list
    }

    return render(request, 'display_teacher.html', context)

def add_teacher(request):

    form_data = TeacherForm()

    if request.method == 'POST':
        form_data = TeacherForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Teacher Registered Successfully!')
            return redirect('display_teacher')

    context = {
        'title' : 'Register Teacher',
        'page_title' : 'Add Teacher Information',
        'form_data' : form_data,
        'submit_btn_name' : 'Add Teacher',
        'cancel_btn_name' : 'Discard',
        'cancel_btn_url' : 'display_teacher',
    }

    return render(request, 'master/base_form.html', context)
