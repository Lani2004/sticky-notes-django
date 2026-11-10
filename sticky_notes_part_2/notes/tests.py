"""Automated tests for the Sticky Notes application."""

from django.test import TestCase
from django.urls import reverse
from .forms import NoteForm
from .models import Note


class NoteModelTests(TestCase):
    """Verify that notes store their data correctly."""

    def setUp(self):
        self.note = Note.objects.create(
            title='Test Note', content='Test content'
        )

    def test_title(self):
        self.assertEqual(self.note.title, 'Test Note')

    def test_content(self):
        self.assertEqual(self.note.content, 'Test content')

    def test_string_representation(self):
        self.assertEqual(str(self.note), 'Test Note')

    def test_timestamps(self):
        self.assertIsNotNone(self.note.created_at)
        self.assertIsNotNone(self.note.updated_at)


class NoteFormTests(TestCase):
    """Verify that note forms reject incomplete input."""

    def test_valid_form(self):
        form = NoteForm(data={'title': 'Hello', 'content': 'World'})
        self.assertTrue(form.is_valid())

    def test_missing_title(self):
        form = NoteForm(data={'title': '', 'content': 'World'})
        self.assertFalse(form.is_valid())

    def test_missing_content(self):
        form = NoteForm(data={'title': 'Hello', 'content': ''})
        self.assertFalse(form.is_valid())

    def test_title_too_long(self):
        self.assertFalse(
            NoteForm(data={'title': 'x' * 201, 'content': 'World'}).is_valid()
        )


class NoteViewTests(TestCase):
    """Exercise the note CRUD workflow through HTTP requests."""

    def setUp(self):
        self.note = Note.objects.create(
            title='Original', content='First version'
        )

    def test_list_displays_note(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Original')
        self.assertContains(response, 'First version')

    def test_empty_list(self):
        Note.objects.all().delete()
        response = self.client.get(reverse('note_list'))
        self.assertContains(response, 'No notes yet')

    def test_create_form_loads(self):
        self.assertEqual(
            self.client.get(reverse('note_create')).status_code,
            200,
        )

    def test_create_note(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note', 'content': 'New content'
        })
        self.assertRedirects(response, reverse('note_list'))
        self.assertTrue(Note.objects.filter(title='New Note').exists())

    def test_invalid_create_does_not_save(self):
        response = self.client.post(reverse('note_create'), {
            'title': '', 'content': 'New content'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 1)

    def test_edit_form_loads(self):
        response = self.client.get(reverse('note_update', args=[self.note.pk]))
        self.assertContains(response, 'Original')

    def test_edit_note(self):
        url = reverse('note_update', args=[self.note.pk])
        response = self.client.post(
            url,
            {'title': 'Updated', 'content': 'Second version'}
        )
        self.assertRedirects(response, reverse('note_list'))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated')
        self.assertEqual(self.note.content, 'Second version')

    def test_invalid_edit_preserves_note(self):
        url = reverse('note_update', args=[self.note.pk])
        response = self.client.post(
            url,
            {'title': '', 'content': 'Changed'}
        )
        self.assertEqual(response.status_code, 200)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Original')

    def test_delete_confirmation_does_not_delete(self):
        response = self.client.get(reverse('note_delete', args=[self.note.pk]))
        self.assertContains(response, 'Original')
        self.assertTrue(Note.objects.filter(pk=self.note.pk).exists())

    def test_delete_note(self):
        response = self.client.post(
            reverse('note_delete', args=[self.note.pk])
        )
        self.assertRedirects(response, reverse('note_list'))
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())

    def test_missing_edit_returns_404(self):
        response = self.client.get(reverse('note_update', args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_missing_delete_returns_404(self):
        response = self.client.get(reverse('note_delete', args=[99999]))
        self.assertEqual(response.status_code, 404)
