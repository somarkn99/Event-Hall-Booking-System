
# Event Hall Booking System

A backend system for managing event hall bookings.  
This project provides APIs for user registration, authentication, role management, hall management, booking reservations, payment handling, and email notifications.

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
- Email Notifications (SMTP + HTML Templates)
- Standardized API Responses
- Global Exception Handling & Logging
- Custom Pagination Format

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
| Booking System (CRUD and Status Management) | ✅ Completed |
| Payment System | ✅ Completed |
| Email Notification System (HTML templates) | ✅ Completed |
| Standardized API Responses | ✅ Completed |
| Global Exception Handling & Logging | ✅ Completed |
| Custom Pagination Format | ✅ Completed |
| .env Environment Management | ✅ Completed |
---

## 🚀 Setup Instructions

Follow the previously detailed setup instructions for local development.


---

## 📦 Environment Variables (.env)

This project uses `python-decouple` to manage environment variables.  
You must create a `.env` file based on the provided `.env.example`.

### Example `.env`:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=127.0.0.1,localhost

POSTGRES_DB=event_hall_db
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgres://your_db_user:your_db_password@db:5432/event_hall_db

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.yourprovider.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```

---

## 🐳 Docker Development Setup

### Prerequisites

- Install Docker and Docker Compose on your machine.

### Running the project

1. Create a `requirements.txt` file if not exists:

   ```bash
   pip freeze > requirements.txt
   ```

2. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

3. Access the application:

   - Django app: `http://localhost:8000`
   - PostgreSQL DB: running inside the `db` service.

### Container Services

| Service | Description |
| :--- | :--- |
| db | PostgreSQL Database (Container) |
| web | Django Application (Container) |

### Useful Commands

- Enter Django container shell:

  ```bash
  docker exec -it event_hall_web bash
  ```

- Enter PostgreSQL container:

  ```bash
  docker exec -it event_hall_db psql -U your_db_user -d event_hall_db
  ```

---

## 🐳 Docker Production Setup

### Running the project for Production

```bash
docker-compose -f docker-compose.prod.yml up --build
```

- Services:
  - **db**: PostgreSQL Database
  - **web**: Django Application via Gunicorn
  - **nginx**: Reverse proxy serving the Django app

- Application accessible at: `http://your_server_ip_or_domain/`

---
## 📦 API Response Format (Standardized)

All API responses follow a consistent structure:

### 📋 Success Response

```json
{
    "success": true,
    "message": "Action completed successfully",
    "data": { ... }
}
```

### 📋 Error Response

```json
{
    "success": false,
    "message": "An error occurred",
    "errors": { "field_name": ["error detail"] }
}
```

---

## ⚙️ Global Exception Handling

All exceptions (Authentication Errors, Validation Errors, 404 Not Found, 500 Server Errors) are handled using a global custom exception handler.  
Unexpected server errors are logged automatically into the `/logs/error.log` file for future investigation.

---

## 📄 Custom Pagination Format

List APIs with pagination now return a consistent, user-friendly structure:

```json
{
    "success": true,
    "message": "Data retrieved successfully",
    "data": {
        "count": 100,
        "next": "http://api.example.com/resource?page=2",
        "previous": null,
        "results": [
            { ... },
            { ... }
        ]
    }
}
```

This ensures smooth integration with frontend applications.

---

## 📬 Contact

For inquiries or contributions, please contact:  
`contact@somar-kesen.com`

---