from  django.forms import  ModelForm, Form
from . import models
from  django import forms

from  django.http import HttpResponse

class Feedback(ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback','film_id']
        widgets={'film_id':forms.HiddenInput()}