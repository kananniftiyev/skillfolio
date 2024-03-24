from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from .serializers import *
from django.contrib.auth import authenticate


# Create your views here.

# User Auth

class LoginView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        if 'jwt' in request.COOKIES:
            return JsonResponse({'message': 'Already logged in'})

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            response = JsonResponse(
                {
                    'message': 'Logged in successfully'
                }
            )

            response.set_cookie(key='jwt', value=str(refresh.access_token), httponly=True)
            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = JsonResponse({
                'message': 'User created successfully',
            })

            response.set_cookie(key='jwt', value=str(refresh.access_token), httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):

        if 'jwt' not in request.COOKIES:
            return JsonResponse({'error': 'Already logged out'})

        try:
            response = JsonResponse({'message': "Logged out successfully"}, status=status.HTTP_200_OK)
            response.delete_cookie(key='jwt')
            return response
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PortfolioView(APIView):
    """
    Write This up.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, slug):
        """
        :param request:
        :param slug:
        :return:
        """
        # TODO: Get username via JWT
        user_instance = get_object_or_404(User, username=slug)
        portfolio_instance = get_object_or_404(Portfolio, slug=slug)
        projects_queryset = Projects.objects.filter(user=user_instance)

        user_serializer = UserSerializer(user_instance)
        portfolio_serializer = PortfolioSerializer(portfolio_instance)

        # Serialize skills for each project
        projects_with_skills_data = []
        for project_instance in projects_queryset:
            # First get skills for specific project then serialize it.
            # After that in project_data serializer dict add new key and value for skills.
            # Then append it to list, so we can iterate over other projects too.
            skills = Skills.objects.filter(project=project_instance)
            skills_data = SkillSerializer(skills, many=True).data

            project_data = ProjectSerializer(project_instance).data
            project_data['skills'] = skills_data

            projects_with_skills_data.append(project_data)

        data = {
            'user': user_serializer.data,
            'portfolio': portfolio_serializer.data,
            'projects': projects_with_skills_data
        }

        return Response(data, status=status.HTTP_200_OK)
