from django.forms import ModelForm, BaseModelForm, BaseForm, CharField
from .models import Developer, User

__author__ = 'nonamenix'


class DeveloperForm(ModelForm):
    class Meta:
        model = Developer


class UserForm(ModelForm):
    class Meta:
        model = User