# LibraryProject

This is a simple Django project created as part of the Introduction to Django project in ALX.

To run:
- python manage.py runserver

---

##
---
Alx_DjangoLearnLab/
└── Introduction_to_Django/
├── bookshelf/
├── create.md
├── retrieve.md
├── update.md
├── delete.md
└── CRUD_operations.md

---

# Managing Permissions and Groups in Django

## Permissions Defined
- can_view: Allow viewing books
- can_create: Allow creating new books
- can_edit: Allow editing books
- can_delete: Allow deletion of books

## Groups
- Viewers: Have only can_view permission
- Editors: Have can_edit and can_create permissions
- Admins: All permissions

## Usage in Views
- The @permission_required decorator was used to protect views based on the permissions granted.

Translated with DeepL.com (free version)