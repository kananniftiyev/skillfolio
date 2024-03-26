import jwt
from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from utils import *
from .models import *
from .serializers import *
from django.contrib.auth import authenticate


# Create your views here.
class LoginView(APIView):
    """
    View for user login. Validates user credentials and issues JWT token upon successful authentication.
    """
    renderer_classes = [JSONRenderer]

    def post(self, request):
        """
        Handle POST request for user login.

        Parameters:
            - request (HttpRequest): HTTP request object containing user credentials.

        Returns:
            - JsonResponse: JSON response indicating successful login or error message.
        """
        jwt_token = request.COOKIES.get('jwt')

        # TODO: Check if this works.
        if jwt_token and is_jwt_valid(jwt_token):
            return JsonResponse({'message': 'Already logged in'})

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            jwt_token = jwt.encode({'username': username, 'exp': JWT_EXP_DATE}, JWT_SECRET_KEY, algorithm='HS256')

            response = JsonResponse({'message': 'Logged in successfully'})

            response.set_cookie(key='jwt', value=jwt_token, httponly=True, expires=JWT_EXP_DATE)
            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    """
    API view for user registration.
    """
    renderer_classes = [JSONRenderer]

    def post(self, request):
        """
        Handle POST request for user registration.

        Parameters:
            - request (HttpRequest): HTTP request object containing user data.

        Returns:
            - JsonResponse: JSON response indicating successful user creation or error message.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            jwt_token = jwt.encode({'username': user.username, 'exp': JWT_EXP_DATE}, JWT_SECRET_KEY,
                                   algorithm='HS256')
            response = JsonResponse({
                'message': 'User created successfully',
            })

            response.set_cookie(key='jwt', value=str(jwt_token), httponly=True, expires=JWT_EXP_DATE)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    API view for logging out a user by removing JWT token from cookies.
    """

    renderer_classes = [JSONRenderer]

    def post(self, request):
        """
        Handle POST request for user logout.

        Parameters:
            - request (HttpRequest): HTTP request object.

        Returns:
            - JsonResponse: JSON response indicating successful logout or error message.
        """

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
    API view for retrieving portfolio details of a user including their projects and skills.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, slug):
        """
        Handle GET request to retrieve portfolio.

        Parameters:
        - request (HttpRequest): HTTP request object.
        - slug (str): Unique identifier for the user's portfolio.

        Returns:
        - Response: JSON response containing user details, portfolio details, projects, and associated skills.
        """
        user_instance = get_object_or_404(User, username=slug)
        portfolio_instance = get_object_or_404(Portfolio, slug=slug)
        projects_queryset = Projects.objects.filter(user=user_instance)

        user_serializer = UserSerializer(user_instance)
        portfolio_serializer = PortfolioSerializer(portfolio_instance)

        projects_with_skills_data = []

        for project_instance in projects_queryset:
            skills_queryset = Skills.objects.filter(project=project_instance)
            skills_data = SkillSerializer(skills_queryset, many=True).data

            project_data = ProjectSerializer(project_instance).data
            project_data['skills'] = skills_data

            projects_with_skills_data.append(project_data)

        data = {
            'user': user_serializer.data,
            'portfolio': portfolio_serializer.data,
            'projects': projects_with_skills_data
        }

        return Response(data, status=status.HTTP_200_OK)


# TODO: Return User Details and settings.
class UserView(APIView):
    """
    if jwt cookie is true and jwt does not expire:
        decodeJWTGetUsername()
        getUserOr404(username)
        userSerializer(user)

        return JSONResponse of user details.


    else:
        return message: User Needs to be logged in.
    """
    pass
