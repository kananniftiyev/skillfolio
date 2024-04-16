# Skillfolio-Backend ⚙️

## Table of Contents

- [Installation](#installation) 🛠️
- [Usage](#usage) 🚀
- [Testing](#testing) 🧪

## Installation

### Using Docker 🐳 

1. Clone the repository:
```commandline
git clone https://github.com/kananniftiyev/skillfolio
```
2. Build the Docker image:
```commandline
docker build -t project-name .
```
3. Run the Docker container:
```commandline
docker run -p 8000:8000 project-name
```

The application will be accessible at `http://localhost:8000`.

### Without Docker

1. Clone the repository:
```commandline
git clone https://github.com/kananniftiyev/skillfolio
```
2. Install dependencies:
```commandline
pip install -r requirements.txt
```
3. Make sure you have Redis installed and running. You can download it from the [official website](https://redis.io/download) and follow the installation instructions.
4. Apply migrations:
```commandline
python manage.py migrate
```
5. Create a superuser:
```commandline
python manage.py createsuperuser
```

## Usage

To use the project, follow these steps:

1. Access the admin panel by navigating to `http://localhost:8000/admin` and log in with your superuser credentials.

2. Use the admin panel to manage users, projects, skills, and portfolios.

3. Explore the API endpoints documented in the OpenAPI documentation available at `http://localhost:8000/api/docs`.

4. If you're using caching, ensure that Redis is configured properly. You can configure Redis caching in your Django settings file (`settings.py`) like this:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Adjust this to match your Redis configuration
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

## Testing
To run tests, use the following command:
```commandline
python manage.py test
```
