from django import forms
from .models import CalendarEvent

class EntryForm(forms.ModelForm):
    class Meta:
        model=CalendarEvent
        fields=("name","remarkdate","descriptions","importance",)




'''
    name=forms.CharField(max_length=100)
    remarkdate=forms.DateTimeField()
    descriptions=forms.CharField(widget=forms.Textarea)
'''
