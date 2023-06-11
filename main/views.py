from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import FeedbackForm

def forms (request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Error'

    form = FeedbackForm()
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'main/forms.html', contex)

def about(request):
    return render(request, 'main/about.html')


def index(request):
    return render(request, 'main/index.html')

def submit(request):
    return render(request, 'main/submit.html')

