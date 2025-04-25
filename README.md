
# Event Hall Booking System

A backend system for managing event hall bookings.  
This project provides APIs for user registration, authentication, hall management, booking reservations, and payment handling.

---

## 📌 Project Overview

The system is designed for:
- Clients who want to search for available halls and make reservations.
- Hall owners who want to manage their event halls and track bookings.
- Admins who manage users, halls, and oversee operations.

---

## 🛠️ Technologies Used

- Python 3.10+
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL
- DRF Simple JWT (Authentication)
- drf-yasg (Swagger API Documentation)

---

## 📈 Progress

| Feature | Status |
| :--- | :--- |
| Project setup with Django and PostgreSQL | ✅ Completed |
| Custom User model creation | ✅ Completed |
| JWT Authentication (Register / Login) | ✅ Completed |
| Swagger API Documentation | ✅ Completed |
| Roles & Permissions | 🚧 Coming Next |
| Hall Management (CRUD) | 🚧 Planned |
| Booking System | 🚧 Planned |
| Payment System | 🚧 Planned |

---

## 🚀 Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://your-repo-link.git
   cd event_hall_booking
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database in `config/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'event_hall_db',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the Swagger documentation at:

   ```
   http://127.0.0.1:8000/swagger/
   ```

---

## 📬 Contact

For inquiries or contributions, please contact:  
`contact@somar-kesen.com`

---