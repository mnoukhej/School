# project

## Project Overview


## Folder Structure

<!-- TREE_START -->
```
├── README.md
├── images
│   └── hero-bg.jpg
├── requirements.txt
├── run_server.bat
├── school_project
│   ├── create_superuser.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── media
│   │   └── faculty
│   │       ├── download.jpg
│   │       └── download_1.jpg
│   ├── school_app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_about_faculty_stream_event_image_and_more.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── styles.css
│   │   │   └── images
│   │   │       └── logo.png
│   │   ├── templates
│   │   │   └── school_app
│   │   │       ├── about.html
│   │   │       ├── academics.html
│   │   │       ├── admission.html
│   │   │       ├── contact.html
│   │   │       ├── events.html
│   │   │       ├── faculty_detail.html
│   │   │       ├── faculty_list.html
│   │   │       ├── girls_hostel.html
│   │   │       ├── index.html
│   │   │       ├── inquiry.html
│   │   │       ├── notices.html
│   │   │       ├── notices_and_events.html
│   │   │       ├── notices_events.html
│   │   │       ├── stream_detail.html
│   │   │       └── streams.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── school_project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   ├── images
│   │   │   └── logo.png
│   │   └── js
│   │       ├── main.js
│   │       └── script.js
│   ├── staticfiles
│   │   ├── admin
│   │   │   ├── css
│   │   │   │   ├── autocomplete.css
│   │   │   │   ├── base.css
│   │   │   │   ├── changelists.css
│   │   │   │   ├── dark_mode.css
│   │   │   │   ├── dashboard.css
│   │   │   │   ├── forms.css
│   │   │   │   ├── login.css
│   │   │   │   ├── nav_sidebar.css
│   │   │   │   ├── responsive.css
│   │   │   │   ├── responsive_rtl.css
│   │   │   │   ├── rtl.css
│   │   │   │   ├── vendor
│   │   │   │   │   └── select2
│   │   │   │   │       ├── LICENSE-SELECT2.md
│   │   │   │   │       ├── select2.css
│   │   │   │   │       └── select2.min.css
│   │   │   │   └── widgets.css
│   │   │   ├── img
│   │   │   │   ├── LICENSE
│   │   │   │   ├── README.txt
│   │   │   │   ├── calendar-icons.svg
│   │   │   │   ├── gis
│   │   │   │   │   ├── move_vertex_off.svg
│   │   │   │   │   └── move_vertex_on.svg
│   │   │   │   ├── icon-addlink.svg
│   │   │   │   ├── icon-alert.svg
│   │   │   │   ├── icon-calendar.svg
│   │   │   │   ├── icon-changelink.svg
│   │   │   │   ├── icon-clock.svg
│   │   │   │   ├── icon-deletelink.svg
│   │   │   │   ├── icon-hidelink.svg
│   │   │   │   ├── icon-no.svg
│   │   │   │   ├── icon-unknown-alt.svg
│   │   │   │   ├── icon-unknown.svg
│   │   │   │   ├── icon-viewlink.svg
│   │   │   │   ├── icon-yes.svg
│   │   │   │   ├── inline-delete.svg
│   │   │   │   ├── search.svg
│   │   │   │   ├── selector-icons.svg
│   │   │   │   ├── sorting-icons.svg
│   │   │   │   ├── tooltag-add.svg
│   │   │   │   └── tooltag-arrowright.svg
│   │   │   └── js
│   │   │       ├── SelectBox.js
│   │   │       ├── SelectFilter2.js
│   │   │       ├── actions.js
│   │   │       ├── admin
│   │   │       │   ├── DateTimeShortcuts.js
│   │   │       │   └── RelatedObjectLookups.js
│   │   │       ├── autocomplete.js
│   │   │       ├── calendar.js
│   │   │       ├── cancel.js
│   │   │       ├── change_form.js
│   │   │       ├── collapse.js
│   │   │       ├── core.js
│   │   │       ├── filters.js
│   │   │       ├── inlines.js
│   │   │       ├── jquery.init.js
│   │   │       ├── nav_sidebar.js
│   │   │       ├── popup_response.js
│   │   │       ├── prepopulate.js
│   │   │       ├── prepopulate_init.js
│   │   │       ├── theme.js
│   │   │       ├── urlify.js
│   │   │       └── vendor
│   │   │           ├── jquery
│   │   │           │   ├── LICENSE.txt
│   │   │           │   ├── jquery.js
│   │   │           │   └── jquery.min.js
│   │   │           ├── select2
│   │   │           │   ├── LICENSE.md
│   │   │           │   ├── i18n
│   │   │           │   │   ├── af.js
│   │   │           │   │   ├── ar.js
│   │   │           │   │   ├── az.js
│   │   │           │   │   ├── bg.js
│   │   │           │   │   ├── bn.js
│   │   │           │   │   ├── bs.js
│   │   │           │   │   ├── ca.js
│   │   │           │   │   ├── cs.js
│   │   │           │   │   ├── da.js
│   │   │           │   │   ├── de.js
│   │   │           │   │   ├── dsb.js
│   │   │           │   │   ├── el.js
│   │   │           │   │   ├── en.js
│   │   │           │   │   ├── es.js
│   │   │           │   │   ├── et.js
│   │   │           │   │   ├── eu.js
│   │   │           │   │   ├── fa.js
│   │   │           │   │   ├── fi.js
│   │   │           │   │   ├── fr.js
│   │   │           │   │   ├── gl.js
│   │   │           │   │   ├── he.js
│   │   │           │   │   ├── hi.js
│   │   │           │   │   ├── hr.js
│   │   │           │   │   ├── hsb.js
│   │   │           │   │   ├── hu.js
│   │   │           │   │   ├── hy.js
│   │   │           │   │   ├── id.js
│   │   │           │   │   ├── is.js
│   │   │           │   │   ├── it.js
│   │   │           │   │   ├── ja.js
│   │   │           │   │   ├── ka.js
│   │   │           │   │   ├── km.js
│   │   │           │   │   ├── ko.js
│   │   │           │   │   ├── lt.js
│   │   │           │   │   ├── lv.js
│   │   │           │   │   ├── mk.js
│   │   │           │   │   ├── ms.js
│   │   │           │   │   ├── nb.js
│   │   │           │   │   ├── ne.js
│   │   │           │   │   ├── nl.js
│   │   │           │   │   ├── pl.js
│   │   │           │   │   ├── ps.js
│   │   │           │   │   ├── pt-BR.js
│   │   │           │   │   ├── pt.js
│   │   │           │   │   ├── ro.js
│   │   │           │   │   ├── ru.js
│   │   │           │   │   ├── sk.js
│   │   │           │   │   ├── sl.js
│   │   │           │   │   ├── sq.js
│   │   │           │   │   ├── sr-Cyrl.js
│   │   │           │   │   ├── sr.js
│   │   │           │   │   ├── sv.js
│   │   │           │   │   ├── th.js
│   │   │           │   │   ├── tk.js
│   │   │           │   │   ├── tr.js
│   │   │           │   │   ├── uk.js
│   │   │           │   │   ├── vi.js
│   │   │           │   │   ├── zh-CN.js
│   │   │           │   │   └── zh-TW.js
│   │   │           │   ├── select2.full.js
│   │   │           │   └── select2.full.min.js
│   │   │           └── xregexp
│   │   │               ├── LICENSE.txt
│   │   │               ├── xregexp.js
│   │   │               └── xregexp.min.js
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── script.js
│   └── templates
│       ├── 404.html
│       ├── 500.html
│       └── base.html
├── script.js
├── setup.bat
└── update_tree.py
```
<!-- TREE_END -->


## 🚀 Installation

### For Linux / macOS

1. Clone the repository:
   ```bash
   git clone https://github.com/mnoukhej/.git

2. Run the setup script (Windows only):
   ```bash
   ./setup.bat


## 📦 Dependencies
<!-- - Python 3.7+
- pandas
- openpyxl
- numpy -->

## 🔧 Configuration

