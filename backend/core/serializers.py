from rest_framework import serializers

from core import models


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'linkedin', 'resume', 'about']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'