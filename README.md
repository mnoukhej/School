# Solpara High School Website

A comprehensive website for Solpara High School built with Django and modern web technologies.

## Features

- School information and about section
- Academic programs overview
- Notice board for important announcements
- Events calendar
- Online inquiry form
- Admin panel for content management

## Technical Stack

- Python 3.8+
- Django 5.0.1
- SQLite (database)
- HTML5, CSS3, JavaScript
- Font Awesome for icons
- Google Fonts

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd school-website
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Admin Access

To access the admin panel:
1. Go to http://127.0.0.1:8000/admin
2. Log in with your superuser credentials
3. Manage notices, events, and inquiries

## Project Structure

```
school_project/
├── manage.py
├── requirements.txt
├── README.md
├── school_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── school_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── base.html
└── static/
    ├── css/
    ├── js/
    └── images/
```

## Features to Add

- Student portal
- Online admission system
- Results management system
- Teacher profiles
- Photo gallery
- News and updates section

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
