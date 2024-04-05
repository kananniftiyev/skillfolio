from typing import Union, Dict, Any

from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .jwt import *
from .models import *
from .serializers import *
from .utils import *

# Type aliases
JSONResponse = Union[JsonResponse, Response]
RequestData = Dict[str, Any]


# Create your views here.
class LoginView(BaseView):
    """
    View for user login. Validates user credentials and issues JWT token upon successful authentication.
    """

    def post(self, request) -> JSONResponse:
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


class RegisterView(BaseView):
    """
    API view for user registration.
    """

    def post(self, request) -> JSONResponse:
        """
        Handle POST request for user registration.

        Parameters:
            - request (HttpRequest): HTTP request object containing user data.

        Returns:
            - JsonResponse: JSON response indicating successful user creation or error message.
        """
        User = get_user_model()

        # Extract user data from request
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        linkedin = request.data.get('linkedin')
        resume = request.data.get('resume')
        about = request.data.get('about')

        if not all([username, password, first_name, last_name, email, linkedin, resume, about]):
            return JsonResponse({'error': 'All form data must be entered'}, status=400)

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'User with this username or email already exists'}, status=400)

        # Create user instance
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, linkedin=linkedin,
                    resume=resume, about=about)

        # Set password using set_password method
        user.set_password(password)

        # Save user
        user.save()

        # Generate JWT token
        jwt_token = jwt.encode({'username': user.username, 'exp': JWT_EXP_DATE}, JWT_SECRET_KEY, algorithm='HS256')

        # Create response
        response = JsonResponse({'message': 'User created successfully'})

        # Set JWT token in cookie
        response.set_cookie(key='jwt', value=str(jwt_token), httponly=True, expires=JWT_EXP_DATE)

        return response


class LogoutView(BaseView):
    """
    API view for logging out a user by removing JWT token from cookies.
    """

    def post(self, request) -> JSONResponse:
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


class PortfolioView(BaseView):
    """
    API view for retrieving portfolio details of a user including their projects and skills.
    """

    def get(self, request, slug: str) -> JSONResponse:
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

        data = {'user': user_serializer.data, 'portfolio': portfolio_serializer.data,
                'projects': projects_with_skills_data}

        return Response(data, status=status.HTTP_200_OK)


class PortfolioCreateView(BaseView):
    """
    ApiView for creating new Portfolio
    """

    def post(self, request) -> JSONResponse:
        """
    Handle POST request to create a new portfolio.

    Parameters:
    - request (HttpRequest): HTTP request object containing user data.

    Returns:
    - JsonResponse: JSON response indicating the success or failure of the portfolio creation.
      - If the JWT token is valid and the portfolio is successfully created, returns a JsonResponse
        with a success message and status code 201 (Created).
      - If the JWT token is missing or invalid, returns a JsonResponse with an error message and
        status code 400 (Bad Request).
      - If the portfolio already exists for the user, returns a JsonResponse with an error message
        indicating the portfolio already exists and status code 400 (Bad Request).
      - If there's missing required data in the request, returns a JsonResponse with an error message
        indicating the missing data and status code 400 (Bad Request).
      - If an unexpected error occurs during portfolio creation, returns a JsonResponse with an error
        message indicating the error and status code 500 (Internal Server Error).
    """
        jwt_token = request.COOKIES.get("jwt")

        if jwt_token and is_jwt_valid(jwt_token):
            username = get_username_from_token(jwt_token)
            user_instance = get_object_or_404(User, username=username)
            portfolio_instance = Portfolio.objects.filter(user=user_instance).first()

            if portfolio_instance is not None:
                return JsonResponse({'message': 'Already exists'}, status=status.HTTP_400_BAD_REQUEST)

            del portfolio_instance

            try:
                new_portfolio = Portfolio(user=user_instance, slug=username, title=request.data['title'],
                                          description=request.data['description'])
                new_portfolio.save()
                return JsonResponse({'message': 'Portfolio created'}, status=status.HTTP_201_CREATED)
            except KeyError:
                return JsonResponse({'message': 'Missing required data'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return JsonResponse({'message': str(e)})

        return JsonResponse({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(BaseView):
    def get(self, request) -> JSONResponse:
        """
            Handle GET request to retrieve User.

            Parameters:
                - request (HttpRequest): HTTP request object.

            Returns:
                - Response: JSON response containing user details.
            """
        jwt_token = request.COOKIES.get("jwt")

        if jwt_token and is_jwt_valid(jwt_token):
            username = get_username_from_token(jwt_token)

            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        else:
            return JsonResponse({"message": "User Needs to be logged in."})

    def put(self, request) -> JSONResponse:
        """
        Update user information.
        :param request:
        :return:
        """
        jwt_token = request.COOKIES.get("jwt")

        if jwt_token and is_jwt_valid():
            username = get_username_from_token(jwt_token)
            user = User.objects.get(username=username)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'User Updated.'})
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request) -> JSONResponse:
        """
        Delete user.
        :param request:
        :return:
        """
        jwt_token = request.COOKIES.get("jwt")

        if jwt_token and is_jwt_valid(jwt_token):
            username = get_username_from_token(jwt_token)
            User.objects.filter(username=username).delete()
            return JsonResponse({'message': 'User Deleted.'})

        else:
            return JsonResponse({"message": "User Needs to be logged in."})


class ProjectView(BaseView):
    def post(self, request) -> JSONResponse:
        jwt_token = request.COOKIES.get("jwt")

        if jwt_token and is_jwt_valid(jwt_token):
            username = get_username_from_token(jwt_token)
            user_instance = User.objects.get(username=username)

            try:
                project = Projects(user=user_instance, title=request.data['title'],
                                   description=request.data['description'], link=request.data['link'])
                project.save()
                skills_data = request.data.getlist('skills')

                for skill_name in skills_data[:5]:  # Iterate over the first 5 skills (or less if less than 5 provided)
                    skill = Skills(project=project, name=skill_name)
                    skill.save()

                return JsonResponse({'message': 'Project Added'})
            except Exception as e:
                return JsonResponse({'message': str(e)})

        else:
            return JsonResponse({"message": "User Needs to be logged in."})

    def delete(self, request) -> JSONResponse:
        jwt_token = request.COOKIES.get("jwt")
        if jwt_token and is_jwt_valid(jwt_token):
            username = get_username_from_token(jwt_token)
            user_instance = User.objects.get(username=username)
            title = request.data.get('title')  # Use get() to avoid KeyError

            try:
                project = Projects.objects.filter(title=title, user=user_instance).first()
                if project is None:
                    raise NotFound("Project Not Found")
                project.delete()
                return Response({'message': 'Project Deleted'})  # Return a Response object
            except Projects.DoesNotExist:
                return Response({'message': 'Project not found'}, status=404)  # Return 404 if project not found
            except Exception as e:
                return Response({'message': str(e)}, status=500)  # Return 500 if any other exception occurs
        else:
            return Response({"message": "User Needs to be logged"},
                            status=401)  # Return 401 if user needs to be logged in
