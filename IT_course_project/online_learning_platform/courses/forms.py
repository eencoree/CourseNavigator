from django import forms
from .models import Course, Type, Task, Step, TaskOption


class SingleChoiceTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'option1', 'option2', 'option3', 'option4', 'option5']


class MultipleChoiceTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'option1', 'option2', 'option3', 'option4', 'option5']


class TextAnswerTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'option1']


class TypeChoiceForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Type.objects.all(), empty_label=None)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['task_type']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'type']


class StepForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.none(), required=True)

    class Meta:
        model = Step
        fields = ['title', 'lesson', 'course']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(StepForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['course'].queryset = Course.objects.filter(created_by=user)
