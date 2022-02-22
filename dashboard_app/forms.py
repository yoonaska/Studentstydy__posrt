from dataclasses import field, fields
from django import forms
from .models import *
from django.db import models

class NotesForm(forms.ModelForm):
      
      class Meta:
            model = Notes
            fields = ['title','discrption']