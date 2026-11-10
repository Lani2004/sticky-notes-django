# Sticky Notes — Part 2 Testing Guide

## Automated tests

From the folder containing `manage.py`, activate a Python virtual environment and install dependencies:

```bash
python3 -m venv myenv
source myenv/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py test notes
```

The 20 tests check the Note model, NoteForm, list, create, update and delete views, invalid data, and missing-note responses. The expected final status is `OK` when all tests pass. Record the actual test output after running.

## Manual testing checklist

Start the application:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

Open http://127.0.0.1:8000/ and verify:

- [ ] Empty list displays a helpful message
- [ ] Creating a note displays it in the list
- [ ] Editing a note changes its title and content
- [ ] Deleting a note first displays a confirmation page
- [ ] Cancel on the deletion page preserves the note
- [ ] Confirming deletion removes the note
- [ ] Submitting empty required fields shows form errors
- [ ] CSS styling is applied correctly

These checks must be completed in a browser; they are not claimed as performed here.

## Submission

Include the source project, all three diagrams in `diagrams/`, unit tests in `notes/tests.py`, and `sticky_github.txt` containing your real public GitHub repository URL. Do not submit `myenv`, `venv`, `__pycache__`, or other generated caches. Upload the project to HyperionDev and request review.
