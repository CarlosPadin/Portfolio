from django.shortcuts import render, redirect
from .models import *
from . import forms
import mimetypes
import os
from django.http.response import HttpResponse

# RENDERING THE MAIN TEMPLATE
def home(request):

    School = Education.objects.all().order_by('DateTo')
    Job = WorkExp.objects.all().order_by('DateTo')

    #-----FORM FOR MESSAGES------
    if request.method == 'POST':
        form = forms.createMessage(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home') 
    else:
        form = forms.createMessage()
    #---------------------------

    return render(request, 'index.html', {'Education': School, 'Jobs': Job, 'Form': form})



# DOWNLOAD CV METHOD
def download_file(request, filename=''):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    filename = 'CV.pdf'
    filepath = BASE_DIR + '/assets/' + filename

    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)

    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename

    return response