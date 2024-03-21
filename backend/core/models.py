from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext_lazy as _

from django.db import models

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique = True)
    email = models.EmailField(('email address'), unique = True)
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
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'email', 'linkedin', 'resume', 'about']

    def __str__(self):
        return self.username

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200)

class Skills(models.Model):
    project =models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
