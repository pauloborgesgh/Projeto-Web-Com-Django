from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    
    
    class Meta:
        model = Task
        fields = ( 'rua', 'bairro', 'number', 'obs','date') 
    #img = models.ImageField()