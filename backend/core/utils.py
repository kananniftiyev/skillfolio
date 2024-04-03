from django.http import JsonResponse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from core.jwt import is_jwt_valid, get_username_from_token


class BaseView(APIView):
    renderer_classes = [JSONRenderer]