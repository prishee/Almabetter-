from django import forms
from studentApp.models import Mark

class StudentMarksForm(forms.ModelForm):
  class Meta:
    model = Mark
    fields = '__all__'
