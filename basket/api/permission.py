from rest_framework.permissions import BasePermission, SAFE_METHODS


class BasketPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

