"""Database models for the sticky notes application."""

from django.db import models


# Create your models here.
class Note(models.Model):
    """Represent a sticky note stored in the database."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the note title as its readable representation."""
        return self.title
