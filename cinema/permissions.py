from rest_framework.permissions import (BasePermission,
                                        SAFE_METHODS)


class IsAdminOrIfAuthenticatedReadOnly(
    BasePermission
):
    def has_permission(self, request, view):
        user = request.user

        if user and user.is_staff:
            return True

        if view.__class__.__name__ == "OrderViewSet":
            if request.method in ["GET", "POST"]:
                return user and user.is_authenticated
            return False

        if request.method in SAFE_METHODS:
            return user and user.is_authenticated

        return False
