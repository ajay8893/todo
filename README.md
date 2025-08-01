
# 📝 Django To-Do List App

A simple, full-stack To-Do List application built with Django.  
This app allows users to register, log in, and manage their personal task list — including adding, editing, deleting, and marking tasks as complete.

---

## 🚀 Features

- 🔐 User Registration and Authentication (Signup, Login, Logout)
- ✅ Create, Read, Update, Delete (CRUD) tasks
- 📅 Set due dates and completion status
- 🔒 User-specific tasks (each user sees only their tasks)
- 🖥️ Django Admin integration
- 🧪 CSRF protection and form validation

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates (HTML), CSS (basic)
- **Database:** SQLite (default for Django)

---

## 🖼️ Screenshots

> _(Optional: Add screenshots of your app here)_

---

## 📁 Project Structure

todo_project/
├── todo/
│   ├── templates/
│   │   └── todo/
│   │       ├── home.html
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       ├── task_confirm_delete.html
│   │       ├── login.html
│   │       └── signup.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── manage.py
└── db.sqlite3
