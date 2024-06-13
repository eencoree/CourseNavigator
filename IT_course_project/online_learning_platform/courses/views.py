from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .forms import TypeChoiceForm


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('courses:create_step', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


def create_step(request, course_id=None):
    if request.method == 'POST':
        form = StepForm(request.POST, user=request.user)
        if form.is_valid():
            step = form.save(commit=False)
            step.course_id = form.cleaned_data['course'].id
            step.save()
            return redirect('courses:create_type', step_id=step.id)
    else:
        form = StepForm(user=request.user)
    return render(request, 'courses/create_step.html', {'form': form, 'course_id': course_id})


def create_type(request, step_id):
    if request.method == 'POST':
        form = TypeChoiceForm(request.POST)
        if form.is_valid():
            type_id = form.cleaned_data['type'].id
            return redirect('courses:create_task', step_id=step_id, type_id=type_id)
    else:
        form = TypeChoiceForm()
    course_id = Step.objects.get(id=step_id).course.id
    return render(request, 'courses/create_type.html', {'form': form, 'step_id': step_id, 'course_id': course_id})


def create_task(request, step_id, type_id):
    step = Step.objects.get(id=step_id)

    if request.method == 'POST':
        if type_id == 1:
            form = SingleChoiceTaskForm(request.POST)
        elif type_id == 2:
            form = MultipleChoiceTaskForm(request.POST)
        elif type_id == 3:
            form = TextAnswerTaskForm(request.POST)
        else:
            form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.step = step
            task.type_id = type_id
            task.save()

            if type_id in [1, 2]:
                options = [form.cleaned_data[f'option{i}'] for i in range(1, 6)]
                for option_text in options:
                    if option_text:
                        TaskOption.objects.create(task=task, text=option_text)

            return redirect('courses:create_type', step_id=step_id)
    else:
        if type_id == 1:
            form = SingleChoiceTaskForm()
        elif type_id == 2:
            form = MultipleChoiceTaskForm()
        elif type_id == 3:
            form = TextAnswerTaskForm()
        else:
            form = TaskForm()

    return render(request, 'courses/create_task.html', {'form': form, 'type_id': type_id})


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses/index.html', {'courses': courses})


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})


@login_required
def step_detail(request, step_id):
    step = get_object_or_404(Step, id=step_id)
    tasks = step.tasks.all()
    return render(request, 'courses/step_detail.html', {'step': step, 'tasks': tasks})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    is_choice_task = task.type.id in [1, 2]
    return render(request, 'courses/task_detail.html', {'task': task, 'is_choice_task': is_choice_task})


@login_required
def content_detail(request, course_id, content_id):
    content = get_object_or_404(Content, pk=content_id, course__id=course_id)
    return render(request, 'courses/content_detail.html', {'content': content})


@login_required
def student_course_detail(request, student_course_id):
    student_course = get_object_or_404(StudentCourse, pk=student_course_id)
    return render(request, 'courses/student_course_detail.html', {'student_course': student_course})


@login_required
def step_student_detail(request, step_student_id):
    step_student = get_object_or_404(StepStudent, pk=step_student_id)
    return render(request, 'courses/step_student_detail.html', {'step_student': step_student})
