"""Forms for creating and editing sticky notes."""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Validate and edit a sticky note using a model form."""
    class Meta:
        """Configure the model fields and widgets used by the form."""
        model = Note
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter note title'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your note',
                'rows': 5
            }),
        }
