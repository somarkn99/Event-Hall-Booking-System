
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

---

## 🚀 Setup Instructions

Follow the previously detailed setup instructions.

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

This structure makes API integration much easier for frontend developers.

---

## ⚙️ Global Exception Handling

All exceptions (Authentication Errors, Validation Errors, 404 Not Found, 500 Server Errors) are handled using a global custom exception handler.  
Unexpected server errors are logged automatically into the `/logs/error.log` file for future investigation.

Example of an internal server error log:

```log
ERROR 2025-04-25 22:35:19 exceptions An unhandled exception occurred
Traceback (most recent call last):
  File "...", line ..., in ...
Exception: Detailed error stack trace...
```

---

## 📬 Contact

For inquiries or contributions, please contact:  
`contact@somar-kesen.com`

---