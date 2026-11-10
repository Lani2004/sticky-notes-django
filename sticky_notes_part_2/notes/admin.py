"""Django admin configuration for sticky notes."""

from django.contrib import admin
from .models import Note

# Register your models here.
admin.site.register(Note)
