
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

---

## 🚀 Setup Instructions

Follow the previously detailed setup instructions.

---

## 📬 Email Notification System (HTML Emails)

Email notifications are sent using Django templates for booking confirmation, booking cancellation, and payment receipt events.

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

## 📬 Contact

For inquiries or contributions, please contact:  
`contact@somar-kesen.com`

---