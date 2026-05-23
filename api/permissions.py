from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """Faqat roli 'admin' bo'lgan foydalanuvchilarga ruxsat beradi"""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'admin'
        )