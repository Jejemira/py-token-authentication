from rest_framework.permissions import (BasePermission,
                                        SAFE_METHODS)
from cinema.views import OrderViewSet


class IsAdminOrIfAuthenticatedReadOnly(
    BasePermission
):
    def has_permission(self, request, view):
        if request.method in ("HEAD", "OPTIONS"):
            return True

        user = request.user

        if user and user.is_staff:
            return True

        if isinstance(view, OrderViewSet):
            if request.method in SAFE_METHODS or request.method == "POST":
                return user and user.is_authenticated
            return False

        if request.method in SAFE_METHODS:
            return user and user.is_authenticated

        return False
