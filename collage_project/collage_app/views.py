

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, Student
from .forms import StudentForm

def home(request):
    sections = Section.objects.all()
    return render(request, 'collage_app/home.html', {'sections': sections})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'collage_app/add_student.html', {'form': form})

def view_section(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    students = Student.objects.filter(section=section)
    return render(request, 'collage_app/view_section.html', {'section': section, 'students': students})

def view_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'collage_app/view_student.html', {'student': student})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_section', section_id=student.section.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'collage_app/add_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    section_id = student.section.id
    student.delete()
    return redirect('view_section', section_id=section_id)
