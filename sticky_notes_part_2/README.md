# Sticky Notes Application — Django Part 1

A Django web application for creating, viewing, editing and deleting sticky notes. This project uses Django's Model–View–Template (MVT) structure and SQLite.

## Project structure

- `manage.py` — Django command-line entry point
- `sticky_notes/` — project configuration (`settings.py`, `urls.py`, ASGI and WSGI)
- `notes/` — **Django application**, created with `python manage.py startapp notes`
  - `models.py` — Note model with title, content and timestamps
  - `forms.py` — NoteForm
  - `views.py` — create, list, update and delete views
  - `urls.py` — application URL routes
  - `templates/notes/` — HTML templates
  - `static/notes/styles.css` — CSS stylesheet
  - `migrations/` — database migrations
- `diagrams/` — use case, sequence and class diagrams
- `research_answers.pdf` — Part 2 research answers
- `requirements.txt` — Python dependencies

The `notes` app is included in `INSTALLED_APPS` in `sticky_notes/settings.py`. The project URL configuration includes `notes.urls`.

## Requirements

- Python compatible with the Django version in `requirements.txt`
- pip

## Installation (macOS / Linux)

Open Terminal in the folder containing `manage.py` and run:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

For Windows, activate the environment with `venv\Scripts\activate` instead.

Visit http://127.0.0.1:8000/ to view the application.

## Using the application

1. Open the home page to see your notes.
2. Choose the create-note link to enter a title and content.
3. Edit a note to update its information.
4. Delete a note using the confirmation page.

The application uses SQLite (`db.sqlite3`) and Django migrations. To create new migrations after changing models, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Static files

The stylesheet lives in `notes/static/notes/styles.css`. For deployment-style static collection, run:

```bash
python manage.py collectstatic --noinput
```

Collected files are placed in `staticfiles/`, which is generated and not needed in the submission.

## Submission contents

Submit this project folder with the `notes` app, `sticky_notes` project configuration, diagrams, Part 2 research answers, migration files, README and requirements. Do not submit the `venv/` directory or Python cache files.

## Code style

Python source includes module, class, method and view docstrings and follows PEP 8 conventions.
