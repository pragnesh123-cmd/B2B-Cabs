from rest_framework import permissions


# class JobCostumPermission(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated)