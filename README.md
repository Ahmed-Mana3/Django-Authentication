📝 Django Blog

🚀 Introduction

This is a Django Blog application with authentication and moderation features. Users can:

Register and log in.

Create, view, and delete their own posts.

Visit user profiles.

Moderators have special privileges to:

Delete any post.

Ban or unban users.

----------------------------------

✨ Features

🔑 Authentication: User login/logout & session management.

📝 Post Management: Create, view, and delete blog posts.

👤 User Profiles: View user-specific posts and profiles.

🛡 Moderation Tools: Ban/unban users, delete inappropriate posts.

🎨 Bootstrap UI: Responsive frontend with Bootstrap 5.

----------------------------------

🛠 Tech Stack

Backend: Django 5.2

Frontend: Django Templates + Bootstrap 5

Database: SQLite (default, can be switched to PostgreSQL/MySQL)

Admin Panel: Jazzmin for a modern Django admin interface

----------------------------------

⚙️ Installation
1. Clone the repository
git clone https://github.com/Ahmed-Mana3/Django-Blog.git
cd Django-Blog

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Create a superuser
python manage.py createsuperuser

6. Run the development server
python manage.py runserver


Visit: http://127.0.0.1:8000

----------------------------------

▶️ Usage

Access the homepage to see all posts.

Log in or sign up to create posts.

Visit a user’s profile to see their posts.

Moderators can ban/unban users or delete posts directly from the interface.

----------------------------------

## 📂 Project Structure
```plaintext
Django-Blog/
│── app/                # Main blog app
│   ├── models.py       # Post model
│   ├── views.py        # Blog views
│   ├── urls.py         # Blog routes
│   ├── templates/      # HTML templates
│── users/              # User management app
│── project/            # Main Django project config
│   ├── settings.py     # Django settings
│   ├── urls.py         # Root URLs
│── templates/          # Base templates (Bootstrap)
│── manage.py           # Django CLI


----------------------------------
Thenk you for reading ❤️
