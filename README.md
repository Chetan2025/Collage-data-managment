| **File**                                          | **Purpose**                                                                   |
| ------------------------------------------------- | ----------------------------------------------------------------------------- |
| **collage\_project/urls.py**                      | Project-level URL router. Includes `collage_app.urls`                         |
| **collage\_app/models.py**                        | Defines `Section` and `Student` models                                        |
| **collage\_app/forms.py**                         | Django ModelForm for Student Add/Edit                                         |
| **collage\_app/views.py**                         | Handles logic for Add, Edit, Delete, View Section, View Student               |
| **collage\_app/urls.py**                          | App-specific URLs like `add_student/`, `section/<id>/`, `student/<id>/`, etc. |
| **collage\_app/templates/collage\_app/home.html** | Contains **all frontend HTML design (the code I gave you)**                   |
| **collage\_app/admin.py**                         | For Django Admin panel access (Section, Student)                              |
| **manage.py**                                     | Django run/migrate commands                                                   |


collage_data_aplication/
│
├── collage_env/                 # Your Python Virtual Environment (No need to touch)
│
├── collage_project/
│   ├── collage_project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py              <-- Project Level URLs (include app.urls)
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── collage_app/
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── templates/
│   │   │   └── collage_app/
│   │   │       └── home.html    <-- You will paste the full HTML template here
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py             <-- StudentForm defined here
│   │   ├── models.py            <-- Section & Student Models here
│   │   ├── urls.py              <-- App Level URLs (view mappings)
│   │   └── views.py             <-- All views (home, add_student, edit, delete)
│   │
│   ├── manage.py                <-- Django Management Script
│
├── db.sqlite3                   <-- Your SQLite Database File (auto-created)
└── requirements.txt             <-- (Optional) for pip freeze
