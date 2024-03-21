from rest_framework import serializers

from core import models


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'