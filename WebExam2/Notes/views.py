
from django.shortcuts import render, redirect

from WebExam2.Notes.forms import ProfileForm, NoteForm, DeleteNoteForm
from WebExam2.Notes.models import Profile, Note


# Create your views here.
def home_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    form = ProfileForm()
    if not profile:
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'home-with-profile.html')

        context = {
            'form': form,
            'profile': profile,
        }

        return render(request, 'home-no-profile.html', context)

    context = {
        'form': form,
        'notes': notes,

    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == "GET":
        form = NoteForm()
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'note-create.html', context)


def edit_note(request, id):
    note = Note.objects.filter(pk=id).get()
    if request.method == "GET":
        form = NoteForm(instance=note)
    else:
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, id):
    note = Note.objects.filter(pk=id).get()

    if request.method == "GET":
        form = DeleteNoteForm(instance=note)
    else:
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, id):
    note = Note.objects.filter(pk=id).get()

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)


def profile_page(request):
    profile = Profile.objects.get()
    notes = Note.objects.all()
    form = ProfileForm()

    # if request.method == "POST":
    #     form = DeleteProfileForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         notes.delete()
    #         form.save()
    #         return redirect('index')

    context = {
        'form': form,
        'profile': profile,
        'notes': notes,
    }

    return render(request, 'profile.html', context)


def delete_profile(request):
    user_profile = Profile.objects.first()
    all_notes = Note.objects.all()

    user_profile.delete()
    all_notes.delete()
    return redirect('index')
