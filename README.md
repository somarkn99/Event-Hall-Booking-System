
# Event Hall Booking System

A backend system for managing event hall bookings.  
This project provides APIs for user registration, authentication, role management, hall management, booking reservations, and payment handling.

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
- django-filter (Search / Filter / Ordering)

---

## 📈 Progress

| Feature | Status |
| :--- | :--- |
| Project setup with Django and PostgreSQL | ✅ Completed |
| Custom User model creation | ✅ Completed |
| JWT Authentication (Register / Login) | ✅ Completed |
| Swagger API Documentation | ✅ Completed |
| Roles & Permissions | ✅ Completed |
| Role Assignment API (Admin only) | ✅ Completed |
| Hall Management (CRUD) | ✅ Completed |
| Filtering, Search, and Ordering | ✅ Completed |
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

5. Run migrations and create default roles:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py create_roles
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

## 🛡️ Role Management API

Admins can assign roles to users using the following endpoint:

- **POST /api/accounts/assign-role/**

**Body Example:**

```json
{
  "user_id": 5,
  "role": "Owner"
}
```

**Roles available:**
- Admin
- Owner
- Customer

---

## 🔍 Hall Filtering API

The Hall listing endpoint supports filtering, searching, and ordering.

- **Endpoint:** `/api/halls/`

### 🔎 Supported Filters

| Parameter         | Type     | Description                          |
|------------------|----------|--------------------------------------|
| `location`        | string   | Filter by location                   |
| `capacity`        | number   | Exact match of capacity              |
| `price_per_hour`  | decimal  | Exact match of price                 |
| `search`          | string   | Search in name, description, location |
| `ordering`        | string   | Sort by `price_per_hour`, `capacity` |

### 💡 Examples

- Filter by location:

  ```
  /api/halls/?location=Erbil
  ```

- Search for keyword:

  ```
  /api/halls/?search=luxury
  ```

- Order by price ascending:

  ```
  /api/halls/?ordering=price_per_hour
  ```

- Order by capacity descending:

  ```
  /api/halls/?ordering=-capacity
  ```

---

## 📬 Contact

For inquiries or contributions, please contact:  
`contact@somar-kesen.com`

---