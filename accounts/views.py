from rest_framework.views import APIView
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from accounts.models import User
from accounts.constants import Roles
from accounts.permissions import IsAdmin
from utils.responses import success_response, error_response

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Assign "Customer" role by default
            customer_group = Group.objects.get(name="Customer")
            user.groups.add(customer_group)

            return success_response("User registered successfully", status_code=201)
        return error_response("Registration failed", serializer.errors, status_code=400)

class AssignRoleView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        operation_description="Assign a role to a user (Admin only)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id', 'role'],
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'role': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: 'Role assigned successfully', 400: 'Bad Request'},
    )
    def post(self, request):
        user_id = request.data.get('user_id')
        role_name = request.data.get('role')

        if not user_id or not role_name:
            return error_response("user_id and role are required", status_code=400)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return error_response("User not found", status_code=404)

        if role_name not in dict(Roles.CHOICES):
            return error_response("Invalid role", status_code=400)

        user.groups.clear()
        group = Group.objects.get(name=role_name)
        user.groups.add(group)

        return success_response(f"Role '{role_name}' assigned to user '{user.email}'")
