# Blog Clone App

This is a Django-based blog application that allows users to create, edit, delete, and publish blog posts. The application also includes features such as commenting on posts, approving comments, and user authentication.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Create, Edit, and Delete Posts**: Authenticated users can create new posts, edit existing ones, and delete posts.
- **Commenting**: Users can comment on posts. Comments can be approved by the post author.
- **Post Publishing**: Draft posts can be published by the author.
- **Post Listing and Detail Views**: Users can view a list of all published posts and see details of individual posts.
- **Responsive Design**: The app is designed to be responsive and user-friendly on all devices.

## Installation

### Prerequisites

- Python 3.11
- Django 3.11 or later
- Virtualenv (optional but recommended)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/oyebamijisodiq/blog_clone.git
   cd blog_clone
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Homepage**: View a list of published posts.
- **Post Detail**: Click on a post title to view the post and its comments.
- **Create/Edit Post**: Logged-in users can create and edit their own posts.
- **Delete Post**: Logged-in users can delete their own posts.
- **Commenting**: All users can comment on posts. Comments are pending approval by the post author.
- **Admin Panel**: Accessible to superusers for managing posts, comments, and users.

## Project Structure

```
blog_clone/
│
├── blog/                  # Main application directory
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS, JavaScript, images)
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # View functions and class-based views
│   ├── urls.py            # URL configurations
│   └── ...
│
├── siteclone/             # Project configuration directory
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   └── ...
│
├── manage.py              # Django management script
├── db.sql                 # SQL database file
└── requirements.txt       # Python dependencies
```

## Contributing

If you’d like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add my feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.


## Acknowledgements

- Thanks to the Django community for providing excellent documentation and resources.
- Inspired by the official Django tutorial for building a blog and bought udemy courses.

