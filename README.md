# Django E-Commerce

A simple E-Commerce application built with Django.

## Features

- User Registration
- Login / Logout
- Product Catalog
- Product Detail Page
- Shopping Cart
- Checkout
- Order History
- Admin Panel

## Installation

```bash
git clone <repo-url>
cd django_ecommerce

python -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```
