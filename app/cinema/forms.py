from .models import *
from django import forms
from django.forms import ModelForm, TextInput, Textarea, \
    Select, CheckboxInput, PasswordInput, EmailInput
from tinymce.widgets import TinyMCE


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["type_r"].choices = [("", "Выберите пункт"), ] + list(
            self.fields["type_r"].choices)[0:]

    class Meta:
        model = Comment
        fields = ['name', 'description',
                  'type_r']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
            }),
            "type_r": Select(attrs={
                'class': 'form-select',
            }),
        }
