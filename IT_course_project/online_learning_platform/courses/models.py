from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudentCourse(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_courses')

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"


class ExpertCourse(models.Model):
    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expert_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='expert_courses')

    def __str__(self):
        return f"{self.expert.username} - {self.course.title}"


class CreatorCourse(models.Model):
    course_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       related_name='creator_courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='creator_courses')

    def __str__(self):
        return f"{self.course_creator.username} - {self.course.title}"


class Type(models.Model):
    task_type = models.CharField(max_length=50)

    def __str__(self):
        return self.task_type


class Step(models.Model):
    title = models.CharField(max_length=255)
    lesson = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='steps')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='tasks')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='tasks')
    option1 = models.CharField(max_length=100, blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)
    option5 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class TaskOption(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Content(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE, related_name='contents')
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='contents')

    def __str__(self):
        return self.title


class StepStudent(models.Model):
    answer = models.TextField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='step_students')
    step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='step_students')

    def __str__(self):
        return f"{self.user.username} - {self.step.title}"


class AQ(models.Model):
    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='aqs')
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.expert.username} - {self.question}"
