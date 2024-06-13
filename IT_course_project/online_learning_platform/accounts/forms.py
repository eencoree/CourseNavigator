from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.')
    role = forms.ChoiceField(choices=[('student', 'Student'), ('expert', 'Expert'), ('creator', 'Creator')])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'role')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'role')
