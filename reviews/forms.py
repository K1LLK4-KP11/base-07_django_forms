from django import forms
from django.forms import ModelForm
from .models import book  

class BookForm(ModelForm):  
    class Meta:  
        model = book
        exclude = ['published_date']  
        fields = ['title', 'author', 'description'] 
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Заголовок должен содержать не менее 5 символов.")  
        return title