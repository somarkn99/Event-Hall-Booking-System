from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Owner').exists()

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Customer').exists()
