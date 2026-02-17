
# 🧑‍💻 Django Personal Blog Website (WIP)

A **personal blog website** built with **Django 5**, designed to share articles, categorize content, and allow visitors to contact the site owner.  
This project is under active development and serves as a **personal portfolio & learning project**.

> ⚠️ **Status:** Work in Progress (WIP)  
> Some features are still being improved and new ones will be added.

---

## 🚀 Project Goals

- Build a clean and scalable **Django blog system**
- Practice **Class-Based Views**
- Implement **internationalization (EN / UZ)**
- Create a reusable and powerful **admin panel**
- Prepare the project for future expansion (API, comments, SEO)

---

## ✨ Current Features

### 📝 Blog
- Blog post CRUD via Django Admin
- SEO-friendly **unique slug generation**
- **Many-to-Many categories**
- Post **view counter**
- Automatic **reading time calculation**
- Optional featured image for each post
- Published / unpublished post logic
- Optimized ordering and database indexes

### 📂 Categories
- Multiple categories per post
- Category-based post filtering
- Clean category URLs

### 🔍 Search & Pagination
- Search by title, excerpt, and content
- Pagination for blog list pages

### 📩 Contact System
- Contact form for visitors
- Messages saved in database
- Read / unread message tracking
- Admin panel support

### 🌍 Internationalization (i18n)
- Language support: **English (EN)** and **Uzbek (UZ)**
- URL-based language switching (`/en/`, `/uz/`)
- Django `LocaleMiddleware`
- Template translations
- Multilingual-ready architecture

### 🛠️ Admin Panel
- Custom admin interface
- Image preview in post list
- Filters, search, and ordering
- Bulk publish / unpublish actions
- Read-only analytics fields (views, reading time)

---

## 🧰 Tech Stack

- **Python 3**
- **Django 5.2**
- **PostgreSQL**
- **django-modeltranslation**
- **django-widget-tweaks**
- **Pillow** (required for image handling)

---

## 📂 Project Structure

```

django-blog-website/
├── core/                   # Project settings
├── blogs/                  # Main blog application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── translation.py
├── templates/              # HTML templates
├── static/                 # Static files
├── media/                  # Uploaded images
├── locale/                 # EN / UZ translations
├── manage.py
└── README.md

````


---

## 🗄️ Database Models Overview

### 📌 Category

* Unique category name
* Used for grouping posts

### 📝 Post

* Title & auto-generated slug
* Many-to-many categories
* Optional base image
* Excerpt & full content
* View counter
* Reading time calculation (words / 180)
* Published flag
* Created & updated timestamps

### 📩 ContactMessage

* Name, email, subject, message
* Read/unread status
* Timestamped submissions

---

## ⚙️ Installation & Setup

### 1️⃣ Clone repository

```bash
git clone https://github.com/yourusername/django-blog-website.git
cd django-blog-website
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```


### 3️⃣ Packages

This project uses the following Python packages:

- **Django==5.2** – The main web framework  
- **psycopg2-binary** – PostgreSQL database adapter  
- **python-decouple** – Environment variable and settings management  
- **django-modeltranslation** – For translating model fields (multi-language support)  
- **django-widget-tweaks** – For customizing form widgets in templates  
- **Pillow** – Image processing library for handling uploaded images


### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run development server

```bash
python manage.py runserver
```

---

## 🌍 Translation Commands

```bash
django-admin makemessages -l en
django-admin makemessages -l uz
django-admin compilemessages
```

---

## 🧪 Project Status & Known Gaps

* UI/UX is minimal (focus is backend)
* SEO optimization is basic
* No comment system yet
* Authentication for users not implemented
* Media handling requires Pillow (included)

---

## 🔮 Planned Features

* Post comments
* Rich text editor (CKEditor / TinyMCE)
* REST API (Django REST Framework)
* SEO meta tags
* Deployment (Docker / VPS)
* Dark mode UI

---

## 👤 Author: Mehroj Saparov

Personal Django project built for learning and portfolio purposes.
Focused on **clean architecture**, **scalability**, and **best practices**.

⭐ If you like this project, feel free to star the repository!

