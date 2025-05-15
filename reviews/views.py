from django import forms
from django.shortcuts import render, redirect
from .models import book
from .forms import BookForm
from django.views.generic import ListView  

class book_list(ListView):  
    model = book
    template_name = 'reviews/list.html'  
    context_object_name = 'book'
# Create your views here.
# views.py  

def create_review(request):  
    if request.method == 'POST':  
        form = BookForm(request.POST)  
        if form.is_valid():  
            form.save()  # Saves directly to the database  
            return redirect('book_list')  
            pass
        else:
            errors = form.errors
    else:  
        form = BookForm()  
    return render(request, 'reviews/create.html', {'form': form})  



# Create your views here.
def error_404(request, exception):
    return render(request, '404.html', status=404) 

def error_500(request):
    return render(request, '505.html', status=500)



