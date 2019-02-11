from django.shortcuts import render ,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Notes
from .forms import NotesForm
from django.contrib import messages

# Create your views here.
######################################################
#                  show all Notes                    #
######################################################
def notes(request):
    notes = Notes.objects.all()
    context ={
        'notes': notes
    }
    return render(request,'notes.html',context)
######################################################
#               show one details note                #
######################################################
def note_details(request, slug):
    note_details = Notes.objects.get(slug=slug)
    context ={
        'note_details': note_details
    }
    return render(request,'one_note.html',context)
######################################################
#                     Add note                       #
######################################################
def note_add(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save( )
            messages.success(request,'hihihihih')
            return redirect('/')
    else:
        form = NotesForm()
    context ={'form':form}
    return render(request,'note_add.html',context )
#######################################################
#                     note_edit                       #
#######################################################
def note_edit(request,slug):
    note = get_object_or_404(Notes, slug=slug)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save( )
            return redirect('/')
    else:
        form = NotesForm(instance=note)
    context ={'form':form}
    return render(request,'note_edit.html',context )
