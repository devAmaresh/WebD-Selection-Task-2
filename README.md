# Welcome to my GeekHaven WebD-Selection-Task-2 project GitHub Repository! 👋

## Personal Information
- **Name:** Amaresh Prasad
- **Enrollment Number:** IFI2022023
- **WhatsApp Number:** [Please reach out to me on WhatsApp](https://www.whatsapp.com/)[NA As its public]
- **Preferred Bucket:** Backend Development


# Django Social Media App Documentation

Welcome to the documentation for the Django Social Media App. This documentation provides an overview of the features, setup instructions, and usage details for the app.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [User Registration and Profile](#user-registration-and-profile)
  - [Posts and Comments](#posts-and-comments)
  - [Communities](#communities)
  - [Friendships](#friendships)
- [Admin Panel](#admin-panel)
- [Contributing](#contributing)

## Features

- User registration and profile management.
- Posting content, including text and images.
- Commenting on posts.
- Creating and joining communities to share ideas.
- Sending and accepting friend requests.
- Admin panel for managing users, posts, communities, etc.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python
- Django
- Django Rest Framework

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/devAmaresh/WebD_final.git
   cd WebD_final
2.Run the commands:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
``` 

## Usage

### User Registration and Profile

- Register new users using the `/register/` endpoint.
- View and update user profiles using the `/profile/` endpoint.

### Posts and Comments

- View posts from friends and own posts using the `/posts/` endpoint.
- Create new posts using the `/posts/` endpoint.
- Comment on posts using the `/post-comments/<int:post_id>/` endpoint.

### Communities

- View existing communities and create new ones using the `/communities/` endpoint.
- Join communities and share ideas with members.

### Friendships

- Send friend requests using the `/friend-request/<int:to_user_id>/` endpoint.
- Accept friend requests using the `/accept-friend-request/<int:from_user_id>/` endpoint.

## Admin Panel

Access the Django admin panel at `/admin/` to manage users, posts, communities, and more. You can customize the admin panel's appearance and functionality.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.

## Live Deployed Site

Check out the live version of the social media website: <a href="https://amareshh.pythonanywhere.com/" target="_blank">Deployed site</a>

**Disclaimer:** Please note that this site is still under development. I'm continuously working to improve it, and any feedback or suggestions are welcome!

Feel free to explore my repository to see the progress of my project. If you have any questions or want to connect with me, you can reach me via WhatsApp or through GitHub discussions.

Thank you for visiting my repository! Happy coding! 🚀
