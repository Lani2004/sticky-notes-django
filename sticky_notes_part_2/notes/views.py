"""Request handlers for sticky note CRUD operations."""

from django.shortcuts import get_object_or_404, redirect, render
from .forms import NoteForm
from .models import Note


# Create your views here.
def note_list(request):
    """Display all sticky notes, newest first."""
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {
        'notes': notes
    })


def note_create(request):
    """Display a form and save a new note after validation."""
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {
        'form': form
    })


def note_update(request, pk):
    """Display a form and update the selected note."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('note_list')

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {
        'form': form
    })


def note_delete(request, pk):
    """Confirm and delete a note after a POST request."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('note_list')

    return render(request, 'notes/note_confirm_delete.html', {
        'note': note
    })
