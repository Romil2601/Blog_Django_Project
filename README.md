# ✨ WriteSphere – Django Blogging Platform

WriteSphere is a modern full-stack blogging platform built with Django.  
Users can create blog posts, interact with authors, follow profiles, like posts, and engage through comments.

---

# 🚀 Features

## 🔐 Authentication System
- User Registration
- User Login & Logout
- Protected Routes
- Role-Based Access

---

## 📝 Blog Features
- Create Blog Posts
- Edit & Delete Posts
- Upload Cover Images
- Categories System
- Rich Blog Detail Pages

---

## ❤️ Interaction Features
- Like / Unlike Posts
- Add Comments
- Edit & Delete Comments
- Follow / Unfollow Authors

---

## 👤 User Profiles
- Upload Profile Photos
- Edit Bio
- View User Posts
- Followers & Following Count

---

## 🔍 Search & Pagination
- Search Blogs
- Search Authors
- Search Categories
- Pagination Support

---

## 🛠️ Admin Features
- Django Admin Customization
- Manage Users
- Manage Posts
- Manage Categories
- Manage Comments

---

# 🧰 Tech Stack

## Backend
- Django 5
- Python 3.11

## Frontend
- HTML5
- CSS3
- Bootstrap 5

## Database
- SQLite (Deployment)
- MySQL (Local Development)

## Deployment
- PythonAnywhere

## Version Control
- Git & GitHub

---

# 📂 Project Structure

```bash
WriteSphere/
│
├── blog/
├── writesphere/
├── media/
├── static/
├── staticfiles/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Romil2601/Blog_Django_Project.git
```

---

## 2️⃣ Go To Project Folder

```bash
cd Blog_Django_Project
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run Migrations

```bash
python manage.py migrate
```

---

## 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Start Development Server

```bash
python manage.py runserver
```

---

# 🌐 Deployment

Project deployed using:

- PythonAnywhere
- SQLite
- Gunicorn
- Static File Collection

---

# 📸 Screenshots

## Home Page
- Modern Blog Cards
- Pagination
- Search Bar

## Profile Page
- Circular Profile Images
- Follow System
- User Posts

## Blog Detail Page
- Like System
- Comments Section
- Follow Author

---

# 🔒 Environment Variables

Example `.env`:

```env
SECRET_KEY=your_secret_key
DEBUG=False
```

---

# 📦 Requirements

Generate requirements:

```bash
pip freeze > requirements.txt
```

---

# 📌 Future Improvements

- Rich Text Editor
- Notifications System
- Email Verification
- Dark Mode
- REST API
- Chat System

---

# 👨‍💻 Author

## Romil Raja

- Python Developer
- Django Developer
- Full Stack Learner

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others

---

# 📜 License

This project is open-source and available under the MIT License.
