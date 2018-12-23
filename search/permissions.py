from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # This will always be false as user donot have permission to edit data
        return False
