from django.shortcuts import render, redirect
from courseApp.models import CourseCategoryModel, CourseModel
from courseApp.forms import CourseCategoryForm, CourseForm
from django.contrib import messages


def display_course_category(request):
    course_category_list = CourseCategoryModel.objects.all()

    context = {
        'course_category_list' : course_category_list
    }

    return render(request, 'display_course_category.html', context)


def add_course_category(request):
    form_data = CourseCategoryForm()

    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Course Category Added Successfully!')
            return redirect('display_course_category')

    context = {
        'title' : 'Course Category',
        'page_title' : 'Add Course Category',
        'form_data' : form_data,
        'submit_btn_name' : 'Add Category',
        'cancel_btn_name' : 'Discard',
        'cancel_btn_url' : 'display_course_category',
    }

    return render(request, 'master/base_form.html', context)

def edit_course_category(request, id):
    category_data = CourseCategoryModel.objects.get(id=id)

    form_data = CourseCategoryForm(instance=category_data)

    if request.method == 'POST':
        form_data = CourseCategoryForm(request.POST, instance=category_data)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Course Category Updated Successfully!')
            return redirect('display_course_category')

    context = {
        'title' : 'Course Category',
        'page_title' : 'Edit Course Category',
        'form_data' : form_data,
        'submit_btn_name' : 'Update Category',
        'cancel_btn_name' : 'Discard',
        'cancel_btn_url' : 'display_course_category',
    }

    return render(request, 'master/base_form.html', context)

def delete_course_category(request, id):
    CourseCategoryModel.objects.get(id=id).delete()
    messages.success(request, 'Course Category Deleted Successfully!')
    return redirect('display_course_category')



def display_course(request):
    course_list = CourseModel.objects.all()

    context = {
        'course_list' : course_list
    }

    return render(request, 'display_course.html', context)

def add_course(request):
    form_data = CourseForm()

    if request.method == 'POST':
        form_data = CourseForm(request.POST, request.FILES)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(request, 'Course Added Successfully!')
            return redirect('display_courses')

    context = {
        'title' : 'Courses',
        'page_title' : 'Add Course',
        'form_data' : form_data,
        'submit_btn_name' : 'Add Course',
        'cancel_btn_name' : 'Discard',
        'cancel_btn_url' : 'display_courses',
    }

    return render(request, 'master/base_form.html', context)

def edit_course(request, id):
    course_data = CourseModel.objects.get(id=id)
    form_data = CourseForm(instance=course_data)

    if request.method == 'POST':
        form_data = CourseForm(request.POST, request.FILES, instance=course_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.created_by = request.user
            data.save()
            messages.success(request, 'Course Updated Successfully!')
            return redirect('display_courses')

    context = {
        'title' : 'Courses',
        'page_title' : 'Update Course',
        'form_data' : form_data,
        'submit_btn_name' : 'Update Course',
        'cancel_btn_name' : 'Discard',
        'cancel_btn_url' : 'display_courses',
    }

    return render(request, 'master/base_form.html', context)

def delete_course(request, id):
    CourseModel.objects.get(id=id).delete()
    messages.success(request, 'Course Deleted Successfully!')
    return redirect('display_courses')