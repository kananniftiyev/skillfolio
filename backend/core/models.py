from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from django.db import models


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        email = self.normalize_email(email)
        user = self.model(username=username.strip(), email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(('email address'), unique=True)
    linkedin = models.CharField(max_length=200)
    resume = models.CharField(max_length=200)
    about = models.TextField()

    # Define related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='users_custom')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users_custom',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'linkedin', 'resume', 'about']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Skills(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
