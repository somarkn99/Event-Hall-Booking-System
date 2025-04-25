
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
- Email Notifications (SMTP)

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
| Email Notification System | ✅ Completed |

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

4. Configure your database and email settings in `config/settings.py`:

   ```python
   DATABASES = { ... }
   
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your_email@example.com'
   EMAIL_HOST_PASSWORD = 'your_email_password'
   DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
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

## 📆 Booking System API

### 📋 Available Endpoints:

- **Create a booking** (Customer only):

  ```
  POST /api/bookings/create/
  ```

- **View my bookings** (Customer only):

  ```
  GET /api/bookings/my-bookings/
  ```

- **View all bookings** (Admin only):

  ```
  GET /api/bookings/all/
  ```

- **Update booking status** (Admin only):

  ```
  PATCH /api/bookings/{booking_id}/update-status/
  ```

---

## 💳 Payment System API

### 📋 Available Endpoints:

- **Create a payment** (Customer only):

  ```
  POST /api/payments/create/
  ```

- **View my payments** (Customer only):

  ```
  GET /api/payments/my-payments/
  ```

- **View all payments** (Admin only):

  ```
  GET /api/payments/all/
  ```

---

## 📬 Email Notification System

### 📋 Events triggering Emails:

| Event | Email Recipient | Description |
| :--- | :--- | :--- |
| Booking Confirmed | Customer | Informs the customer that their booking is confirmed |
| Booking Cancelled | Customer | Informs the customer that their booking is cancelled |
| Payment Successful | Customer | Informs the customer that their payment was successful |

Emails are automatically sent after each event.

---

## 📬 Contact

For inquiries or contributions, please contact:  
`contact@somar-kesen.com`

---