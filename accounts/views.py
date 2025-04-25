from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.models import User
from accounts.constants import Roles
from accounts.permissions import IsAdmin


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Assign "Customer" role by default
            customer_group = Group.objects.get(name="Customer")
            user.groups.add(customer_group)

            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignRoleView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]  # فقط Admins

    @swagger_auto_schema(
        operation_description="Assign a role to a user (Admin only)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['user_id', 'role'],
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the user'),
                'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role to assign (Admin, Owner, Customer)'),
            },
        ),
        responses={200: 'Role assigned successfully', 400: 'Bad Request'},
    )
    def post(self, request):
        user_id = request.data.get('user_id')
        role_name = request.data.get('role')

        if not user_id or not role_name:
            return Response({"error": "user_id and role are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if role_name not in dict(Roles.CHOICES):
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)

        # إزالة الأدوار القديمة وإضافة الدور الجديد
        user.groups.clear()
        group = Group.objects.get(name=role_name)
        user.groups.add(group)

        return Response({"message": f"Role '{role_name}' assigned to user '{user.email}'"}, status=status.HTTP_200_OK)
