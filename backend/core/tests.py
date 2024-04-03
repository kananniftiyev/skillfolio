from django.test import TestCase
from rest_framework.test import APITestCase

from .models import *
from .serializers import *

# Model Tests

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            linkedin='linkedin.com/testuser',
            resume='resume link',
            about='About test user'
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password'))

    # Add more tests for other model methods, fields, and relationships

class ProjectModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            linkedin='linkedin.com/testuser',
            resume='resume link',
            about='About test user'
        )
        self.project = Projects.objects.create(
            user=self.user,
            title='Test Project',
            description='Test Description',
            link='https://example.com'
        )

    def test_project_creation(self):
        self.assertEqual(Projects.objects.count(), 1)
        self.assertEqual(self.project.title, 'Test Project')

    # Add more tests for other model methods, fields, and relationships

class SkillModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            linkedin='linkedin.com/testuser',
            resume='resume link',
            about='About test user'
        )
        self.project = Projects.objects.create(
            user=self.user,
            title='Test Project',
            description='Test Description',
            link='https://example.com'
        )
        self.skill = Skills.objects.create(
            project=self.project,
            name='Test Skill'
        )

    def test_skill_creation(self):
        self.assertEqual(Skills.objects.count(), 1)
        self.assertEqual(self.skill.name, 'Test Skill')

    # Add more tests for other model methods, fields, and relationships

class PortfolioModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            linkedin='linkedin.com/testuser',
            resume='resume link',
            about='About test user'
        )
        self.portfolio = Portfolio.objects.create(
            user=self.user,
            slug='testuser',
            title='Test Portfolio',
            description='Test Portfolio Description'
        )

    def test_portfolio_creation(self):
        self.assertEqual(Portfolio.objects.count(), 1)
        self.assertEqual(self.portfolio.title, 'Test Portfolio')


# Serializer Tests
class UserSerializerTestCase(APITestCase):
    def test_user_serializer(self):
        user_data = {
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'linkedin': 'linkedin.com/testuser',
            'resume': 'resume link',
            'about': 'About test user'
        }
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')

    # Add more tests for other serializers

class ProjectSerializerTestCase(APITestCase):
    def test_project_serializer(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            linkedin='linkedin.com/testuser',
            resume='resume link',
            about='About test user'
        )
        project_data = {
            'user': user.pk,
            'title': 'Test Project',
            'description': 'Test Description',
            'link': 'https://example.com'
        }
        serializer = ProjectSerializer(data=project_data)
        self.assertTrue(serializer.is_valid())
        project = serializer.save()
        self.assertEqual(project.title, 'Test Project')

    # Add more tests for other serializers

class PortfolioSerializerTestCase(APITestCase):
    def test_portfolio_serializer(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password',
            first_name='Test',
            last_name='User',
            linkedin='linkedin.com/testuser',
            resume='resume link',
            about='About test user'
        )
        portfolio_data = {
            'user': user.pk,
            'slug': 'testuser',
            'title': 'Test Portfolio',
            'description': 'Test Portfolio Description'
        }
        serializer = PortfolioSerializer(data=portfolio_data)
        self.assertTrue(serializer.is_valid())
        portfolio = serializer.save()
        self.assertEqual(portfolio.title, 'Test Portfolio')
